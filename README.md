# UAE Corporate Tax RAG — a measured experiment, not a demo

A retrieval-augmented question-answering system over the UAE Federal Tax
Authority's official **Corporate Tax General Guide (CTGGCT1, Sept 2023)** — a
125-page regulatory document. Ask a question in plain language, get an answer
grounded **only** in the document, with verifiable page citations.

The point of this project is not "I built a RAG chatbot." It's the
methodology: **I built five versions, evaluated each against a hand-verified
answer key, and measured which one actually answered correctly — and why.**
The headline result is the opposite of what most tutorials sell: the simplest
improved version won, and the heavily-engineered versions lost. This README
shows the evidence.

---

## The headline finding

> Across five versions of increasing complexity, the **simplest improved
> pipeline (Ring 1)** scored highest on every retrieval metric. Adding
> parent-document chunking, multi-query expansion, HyDE, GPT-4o, and an
> answer-verification pass made the system **worse**, not better — and the
> evaluation data shows exactly why.

This is a more credible result than a clean "complexity always helps" story,
because it forced a real diagnosis of *where each technique helped and where it
backfired.*

---

## The experiment

| Version | Pipeline | What it added |
|---|---|---|
| Baseline | Fixed 1000-char chunks, cosine top-4, basic prompt | the measuring stick |
| **Ring 1** | **600-char recursive chunks, cross-encoder reranker, guardrailed prompt** | **the winner** |
| Ring 2 | + multi-query, contextual compression, token budget, LangSmith | retrieval breadth |
| Ring 3 | + parent-document (2000-char) chunking, Example-aware splitting | bigger context |
| Ring 4 | + HyDE, larger reranker, GPT-4o generation, answer verification | maximum complexity |

Every version was scored on the **same 20-question evaluation set** against a
**hand-verified answer key** drawn from the document.

---

## Results (automated eval, answerable questions, ground-truth answer key)

| Metric | Baseline | **Ring 1** | Ring 2 | Ring 3 | Ring 4 |
|---|---|---|---|---|---|
| Faithfulness | 0.44 | **0.75** | 0.71 | 0.59 | 0.50 |
| Answer relevancy | 0.44 | **0.79** | 0.71 | 0.65 | 0.58 |
| Context precision | 0.71 | **0.96** | 0.95 | 0.84 | 0.72 |
| Context recall | 0.65 | **0.95** | 0.91 | 0.78 | 0.67 |
| **Overall** | 0.56 | **0.86** | 0.82 | 0.72 | 0.62 |
| Out-of-scope refused | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

Manual grading (human check of each final answer) tells a consistent story:
Baseline 11/20, Ring 1 17/20, Ring 2 19/20, Ring 3 17/20, Ring 4 17/20. Where
manual and automated scores diverge slightly (Ring 2), it's because manual
grading credits "mostly right" answers that strict ground-truth scoring marks
down — a known property of the two methods, documented rather than hidden.

---

## Why the simple version won (the diagnosis)

The document is **uniform**: every section is dense legal tax language. That
single property explains the whole result.

- **Small 600-char chunks (Ring 1)** each hold roughly one rule. The embedding
  is a clean signal and the reranker can pick precisely. High precision (0.96),
  high recall (0.95).
- **Large 2000-char chunks (Ring 3)** blend several rules into one chunk. The
  embedding becomes a muddy average of multiple topics, so retrieval precision
  drops (0.96 → 0.84) and the reranker — trained on short passages — does worse
  on long ones.
- **HyDE (Ring 4)** rewrites the question into a hypothetical answer before
  searching. It helped when the model's guess was right (it fixed two
  questions) but actively hurt when the guess was wrong — it invented an
  incorrect penalty figure and led retrieval *away* from the correct page on
  others. A technique that gambles on the model's prior knowledge is risky on a
  domain the model doesn't reliably know.
- **Answer verification (Ring 4)** stripped a *correct* figure because it
  appeared inside a worked example rather than as a general statement — a
  too-strict checker removing good content.

The lesson: **the right RAG architecture is a property of the document, not a
ranking of techniques.** Match the tool to the data; let evaluation decide.

---

## Production architecture (Ring 1)

```
PDF ──▶ PyMuPDF loader (keeps page numbers)
     ──▶ recursive split, 600 chars / 100 overlap
     ──▶ OpenAI text-embedding-3-small
     ──▶ Qdrant (in-memory) vector store
question ──▶ embed ──▶ cosine top-20
          ──▶ cross-encoder rerank (ms-marco-MiniLM-L-6-v2) ──▶ top-5
          ──▶ gpt-4o-mini with grounding + guardrail prompt
          ──▶ answer + page citations
```

Served as a **FastAPI** endpoint (index built once at startup) with a **React
(Vite)** frontend that shows the answer and its source pages.

---

## Evaluation methodology

The evaluation is the **only judge of which version wins**. Every other tool is
a diagnostic, never a referee.

- **20-question test set** across five types: simple lookup, conditional,
  multi-hop, describe-your-situation, and out-of-scope traps.
- **Hand-verified answer key** from the document. (An auto-generated key got
  three answers wrong; these were caught and corrected by hand — a reminder
  that a wrong key silently poisons every score.)
- **LLM-as-judge** scoring faithfulness, answer relevancy, context precision,
  context recall — each anchored to the ground-truth answer.
- **Trap questions** are scored on correct refusal, not answer content.

---

## Tooling built (reusable assets)

| Tool | Purpose | Uses an LLM? |
|---|---|---|
| `profile_document.py` | Structural scan + chunk-size cohesion experiment; recommends a strategy and **admits when it can't** | structural part: no; cohesion part: local embeddings |
| `check_chunks.py` | Measures chunk quality: boundary damage, Example integrity, orphans, length consistency | no |
| `fill_answer_key.py` | Drafts an answer key from the full document (then hand-verified) | yes |
| `evaluate_tax_v2.py` | LLM-as-judge evaluation against the verified key, traps handled separately | yes |

A note on the profiler: it is deliberately honest about its limits. On this
uniform document it **declines** to recommend a chunk size, because the signal
isn't there — that decision belongs to the eval. A tool that knows what it
cannot measure is more trustworthy than one that always answers.

---

## Project structure

```
uae-tax-rag/
├── app/            # Ring 1 — the production pipeline
├── api.py          # FastAPI wrapper (build-once, serve-many)
├── frontend/       # React (Vite) UI
├── experiments/    # baseline, ring2, ring3, ring4 + all results (the evidence)
├── eval/           # test set, verified answer key, evaluator, profiler, chunk checker
└── data/           # the CTGGCT1 PDF
```

---

## Running it

**Backend** (Python 3.11+, OpenAI API key in `.env`):

```bash
pip install -r requirements_api.txt
uvicorn api:app --port 8000          # wait for "Application startup complete"
```

**Frontend** (Node.js LTS):

```bash
cd frontend
npm install
npm run dev                          # opens http://localhost:5173
```

Both must run together: the API answers, the UI asks. Interactive API docs are
at `http://localhost:8000/docs`.

For production you would swap the in-memory Qdrant for a persistent Qdrant
server (a one-line change) and host the reranker behind an API.

---

## Limitations (stated plainly)

- Scoped to **one document** (CTGGCT1, Sept 2023). It does not reflect later
  guides or amendments, and answers "this is not covered" for anything outside
  it — by design.
- The evaluation is only as strong as the hand-verified answer key and the
  representativeness of the 20 questions.
- LLM-as-judge scores indicate trends reliably but should not be read as exact
  to the third decimal.

## Disclaimer

This is an engineering demonstration. It is **informational only and not tax
advice.** Always confirm with a qualified tax professional and the current
official FTA guidance before acting.