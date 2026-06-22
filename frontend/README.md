# UAE Corporate Tax RAG — A Measured Experiment in What Actually Improves Retrieval

A retrieval-augmented generation (RAG) system that answers questions about UAE
Corporate Tax, grounded **only** in the Federal Tax Authority's official
*Corporate Tax General Guide* (CTGGCT1, September 2023) — every answer cites the
page it came from.

But the system is the second half of this project. The first half is the part
most RAG demos skip: **I built five versions, measured each against a
hand-verified answer key, and the results overturned the assumption that more
sophistication means better answers.**

---

## TL;DR — the finding

> The **simplest improved version won.** Small focused chunks + a cross-encoder
> reranker + strict prompt guardrails beat four progressively more complex
> versions — including ones with multi-query expansion, parent-child chunking,
> HyDE, a larger reranker, GPT-4o, and an answer-verification pass.
>
> Complexity did not compound. Each advanced technique fixed one problem and
> introduced another; on this document the additions cost more than they paid.

---

## Part 1 — The Experiment

### Setup

- **Document:** UAE FTA Corporate Tax General Guide (CTGGCT1), 125 pages,
  ~270,000 characters, 36 worked calculation examples, heavy cross-referencing.
- **Eval set:** 20 questions across 5 categories — simple lookup, conditional,
  multi-hop, describe-your-business (the real product UX), and trap/out-of-scope
  (where the correct behaviour is to *refuse*).
- **Ground truth:** an answer key written from the document and **hand-verified**.
- **Two evaluators:** manual grading (the human anchor) and a custom LLM-as-judge
  scoring faithfulness, answer relevancy, context precision, and context recall.

### The five versions

| Version | What it added |
|---------|---------------|
| **Baseline** | Naive fixed 1000-char chunks, cosine top-4, basic prompt, in-memory store |
| **Ring 1** | Page-aware loader, 600-char recursive chunks, Qdrant, cosine top-20 → **cross-encoder reranker** top-5, strict 3-rule prompt (explain conditions, never invent numbers, cite the page) |
| **Ring 2** | + multi-query expansion, + contextual compression, + LangSmith tracing, + token budgeting |
| **Ring 3** | + parent-child chunking (2000-char parents / 300-char children), + Example-aware splitting (36 examples kept whole) |
| **Ring 4** | + HyDE query rewriting, + larger embedding & reranker, + section-label prepending, + answer-verification pass, + GPT-4o generation |

### Results (LLM-as-judge, scored against ground truth)

| Metric | Baseline | **Ring 1** | Ring 2 | Ring 3 | Ring 4 |
|--------|---------:|-----------:|-------:|-------:|-------:|
| Faithfulness | 0.441 | **0.753** | 0.706 | 0.588 | 0.500 |
| Answer relevancy | 0.441 | **0.788** | 0.712 | 0.647 | 0.576 |
| Context precision | 0.706 | **0.959** | 0.953 | 0.841 | 0.724 |
| Context recall | 0.647 | **0.947** | 0.912 | 0.782 | 0.671 |
| **Overall** | 0.559 | **0.862** | 0.821 | 0.715 | 0.618 |
| Traps correctly refused | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

Manual grading agreed on the trajectory: Baseline 11/20 → Ring 1 17/20 →
Ring 2 19/20. Manual and automated diverge slightly on Ring 1 vs Ring 2 because
the LLM-judge penalises incompleteness more strictly.

### Why the complex versions lost

- **Parent-child chunking (Ring 3)** produced cleaner boundaries and kept
  examples whole, but on a *uniform* single-topic document, 2000-char chunks
  blend several rules into one embedding — diluting the retrieval signal.
  Context precision fell 0.96 → 0.84.
- **HyDE (Ring 4)** helped when its hypothetical answer was correct (it finally
  surfaced the AED 1,000,000 natural-person threshold) but *hurt* when wrong —
  invented penalty figures steered search away from the correct page.
- **The verification pass (Ring 4)** removed a correct fact because the
  supporting number lived inside a worked example, not a general statement.

The lesson is not "simple beats complex." It is **match the technique to the
document** — this uniform, self-contained regulatory text rewarded small,
focused chunks a reranker can rank precisely.

---

## Part 2 — The Product

Ring 1 — the winner — is wrapped as a working application.

### Architecture

```
            ┌─────────────── FastAPI (api.py) ───────────────┐
            │  startup (once): load PDF -> chunk (600/100) -> │
            │  embed -> Qdrant -> load cross-encoder reranker │
User -> React UI -> POST /ask -> retrieve top-20 (cosine)     │
   (Vite)          │            -> rerank to top-5 (cross-enc)│
                   │            -> grounded prompt + guardrails│
                   <- answer + page citations + source chunks  │
            └──────────────────────────────────────────────────┘
```

The API builds the index **once at startup** and reuses it for every request,
so each question is answered in seconds rather than rebuilding the pipeline.

### Tech stack

Python · FastAPI · LangChain · Qdrant · OpenAI (`text-embedding-3-small`,
`gpt-4o-mini`) · sentence-transformers (cross-encoder reranker) · LangSmith ·
React + Vite.

### Run it

**Backend** (from the project root):
```bash
python -m venv tax-rag && source tax-rag/Scripts/activate   # Windows Git Bash
pip install -r requirements_api.txt
# put your key in .env:  OPENAI_API_KEY=sk-...
# place CTGGCT1 PDF in data/  (download from tax.gov.ae)
uvicorn api:app --port 8000
```

**Frontend** (in a second terminal):
```bash
cd frontend
npm install
npm run dev      # opens http://localhost:5173
```

---

## The tools I built along the way

Reusable diagnostics, each honest about what it can and cannot measure:

- **`profile_document.py`** — scans document structure (examples, tables,
  cross-references, OCR signal) and runs a chunk-size *cohesion experiment*. It
  **reports "no reliable signal" when a document is too uniform to predict chunk
  size**, instead of faking a confident wrong recommendation.
- **`check_chunks.py`** — measures chunk quality beyond avg/min/max: boundary
  damage (chunks cut mid-sentence), Example integrity, orphan fragments, length
  consistency.
- **`evaluate_tax_v2.py`** — a custom LLM-as-judge built because RAGAS had
  unresolved dependency conflicts in this environment. Scores against ground
  truth and handles trap questions correctly (a refusal counts as a pass).

---

## Methodology lessons (the part that matters most)

1. **The evaluation is the only judge of the winner.** Every other tool is a
   *flashlight* that explains *why* something broke — never a *referee* that
   picks the winner.
2. **Profile to form a hypothesis; let the eval confirm or correct it.** Static
   analysis pointed toward large chunks; the eval proved small ones won.
3. **Change one variable at a time** — five clean versions made the comparison
   defensible.
4. **Hand-verify the answer key.** Auto-extraction wrongly marked three
   answerable questions as "not covered"; a wrong key silently poisons every
   score built on it.
5. **Some properties are knowable before building (structure); some only by
   testing (chunk size).** Knowing which is which is the skill.

---

## Honest limitations

- Built on **one document**, dated September 2023 — later amendments and the
  FTA's newer topic-specific guides are not reflected. Not tax advice.
- Uses **in-memory Qdrant** (fine for one document and a demo; swap for a
  persistent server in production — a one-line change).
- Two questions stayed hard across all versions: the natural-person AED 1M
  turnover threshold (a retrieval problem) and free-zone-to-mainland sales.
- The LLM-as-judge is a *proxy* for correctness; the hand-verified manual grade
  is the more trustworthy anchor. Neither is treated as absolute.

---

*Informational project. Answers are drawn solely from the FTA Corporate Tax
General Guide and must not be relied on as tax advice.*