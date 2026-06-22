"""
api.py — FastAPI wrapper around the Ring 1 RAG system (the eval winner).

WHAT'S DIFFERENT FROM ring1_rag.py (and why):
─────────────────────────────────────────────────────────────────────────
The script (ring1_rag.py) rebuilt the index every run and answered 20
questions from a spreadsheet. An API must instead:

  1. Build the index ONCE when the server starts (load PDF, chunk, embed,
     build Qdrant, load reranker). This is slow (~30s) but happens once.
  2. Keep that index in memory.
  3. Answer ONE question per HTTP request, fast, reusing the warm index.

So the heavy setup moves to startup; each request just retrieves + answers.

The RAG LOGIC is identical to Ring 1 — same chunking (600/100), same
reranker, same grounding prompt with guardrails. We are exposing the
winner, not changing it.

ENDPOINTS:
  GET  /health          → is the server up and the index built?
  POST /ask             → { "question": "..." } → { answer, citations, chunks }

RUN:
  pip install fastapi uvicorn
  uvicorn api:app --reload --port 8000

  Then open http://localhost:8000/docs for an interactive test page.
"""

import os
import numpy as np
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from openai import OpenAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import CrossEncoder

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ─────────────────────────────────────────────────────────────────────────────
# Config — identical to Ring 1 (the eval winner)
# ─────────────────────────────────────────────────────────────────────────────
PDF_PATH       = os.getenv("PDF_PATH", "data/CT General Guide - EN - 10 09 2023.pdf")
CHUNK_SIZE     = 600
CHUNK_OVERLAP  = 100
TOP_K_COSINE   = 20
TOP_K_RERANK   = 5
EMBED_MODEL    = "text-embedding-3-small"
CHAT_MODEL     = "gpt-4o-mini"
COLLECTION     = "uae_tax"
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

client = OpenAI()

# Module-level store for the warm index (built once at startup)
STATE = {"qdrant": None, "reranker": None, "ready": False}


# ─────────────────────────────────────────────────────────────────────────────
# Ring 1 logic (unchanged)
# ─────────────────────────────────────────────────────────────────────────────
def load_and_chunk(pdf_path: str) -> list[dict]:
    loader = PyMuPDFLoader(pdf_path)
    pages  = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    docs = splitter.split_documents(pages)
    chunks = []
    for doc in docs:
        text = doc.page_content.strip()
        if not text:
            continue
        chunks.append({
            "text":   text,
            "page":   doc.metadata.get("page", 0) + 1,
            "source": os.path.basename(pdf_path),
        })
    return chunks


def embed_texts(texts: list[str]) -> np.ndarray:
    vectors = []
    BATCH = 100
    for i in range(0, len(texts), BATCH):
        resp = client.embeddings.create(model=EMBED_MODEL, input=texts[i:i + BATCH])
        vectors.extend(d.embedding for d in resp.data)
    arr   = np.array(vectors, dtype=np.float32)
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms[norms == 0] = 1e-9
    return arr / norms


def build_qdrant(chunks: list[dict], embeddings: np.ndarray) -> QdrantClient:
    qdrant = QdrantClient(":memory:")
    dim    = embeddings.shape[1]
    qdrant.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
    points = [
        PointStruct(
            id=i, vector=embeddings[i].tolist(),
            payload={"text": chunks[i]["text"], "page": chunks[i]["page"],
                     "source": chunks[i]["source"]},
        )
        for i in range(len(chunks))
    ]
    qdrant.upsert(collection_name=COLLECTION, points=points)
    return qdrant


def retrieve_and_rerank(qdrant, reranker, question: str) -> list[dict]:
    q_vec    = embed_texts([question])[0]
    response = qdrant.query_points(
        collection_name=COLLECTION,
        query=q_vec.tolist(),
        limit=TOP_K_COSINE,
        with_payload=True,
    )
    results = response.points
    pairs   = [(question, r.payload["text"]) for r in results]
    scores  = reranker.predict(pairs)
    ranked  = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)[:TOP_K_RERANK]
    return [
        {
            "rank":  i + 1,
            "page":  hit.payload["page"],
            "score": round(float(score), 4),
            "text":  hit.payload["text"],
        }
        for i, (hit, score) in enumerate(ranked)
    ]


GROUNDING_PROMPT = """You are a UAE Corporate Tax assistant. Answer using ONLY the context below.

Rules:
1. If the answer depends on conditions, explain those conditions clearly
   using only the context — do NOT say "I don't know" just because the
   answer is not a simple yes/no.
2. Never state a specific AED amount, penalty figure, percentage, or date
   unless it appears word-for-word in the context below.
3. If the question is genuinely not covered by the context, say:
   "This is not covered in the provided document."
4. End every answer with: Source: page [N] of CTGGCT1.

Context:
{context}

Question: {question}
Answer:"""


def answer_question(question: str) -> dict:
    retrieved = retrieve_and_rerank(STATE["qdrant"], STATE["reranker"], question)
    context   = "\n\n".join(f"[page {r['page']}] {r['text']}" for r in retrieved)
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0,
        messages=[{"role": "user",
                   "content": GROUNDING_PROMPT.format(context=context, question=question)}],
    )
    answer    = resp.choices[0].message.content.strip()
    citations = sorted({r["page"] for r in retrieved})
    return {"answer": answer, "citations": citations, "chunks": retrieved}


# ─────────────────────────────────────────────────────────────────────────────
# FastAPI app — build the index ONCE at startup
# ─────────────────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # runs once when the server starts
    print("Building index (one-time startup)...")
    chunks     = load_and_chunk(PDF_PATH)
    embeddings = embed_texts([c["text"] for c in chunks])
    STATE["qdrant"]   = build_qdrant(chunks, embeddings)
    STATE["reranker"] = CrossEncoder(RERANKER_MODEL)
    STATE["ready"]    = True
    print(f"Ready. {len(chunks)} chunks indexed.")
    yield
    # (nothing to clean up — in-memory store dies with the process)


app = FastAPI(title="UAE Corporate Tax RAG (Ring 1)", lifespan=lifespan)

# Allow the React dev server to call this API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok", "index_ready": STATE["ready"]}


@app.post("/ask")
def ask(req: AskRequest):
    q = (req.question or "").strip()
    if not q:
        return {"error": "Please provide a question."}
    if not STATE["ready"]:
        return {"error": "Index is still building, try again in a moment."}
    return answer_question(q)