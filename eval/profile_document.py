"""
profile_document.py (v2) — Profile a document before building a RAG pipeline.

This version is HONEST about what it can and cannot know:

  PART A — STRUCTURAL SCAN  (mechanical: counting + regex, no model, instant, free)
    Reports FACTS it can measure reliably: examples, tables, code,
    cross-references, headings, OCR signal. Trust these.

  PART B — CHUNK-SIZE EXPERIMENT  (uses a small local embedding model)
    Does NOT guess chunk size from paragraph length (the old mistake).
    Instead it MEASURES, at several candidate sizes, whether a chunk holds
    ONE coherent idea or several mixed ones — then recommends the largest
    size that still stays coherent. This is EVIDENCE, not a guarantee:
    your eval set has the final word.

WHY THE SPLIT:
─────────────────────────────────────────────────────────────────────────
The old version measured PHYSICAL paragraph length and treated it as IDEA
length. Those aren't the same — one big paragraph can hold five small rules.
That's why it wrongly recommended large chunks for the UAE tax doc when
small chunks actually won. Idea size is a question about MEANING, and the
only way to measure meaning is with embeddings. So Part B uses embeddings.

DOES IT NEED AN LLM?
─────────────────────────────────────────────────────────────────────────
- Part A: no model at all. Pure measurement.
- Part B: needs an EMBEDDING model (not a chat LLM). Runs locally and free
  with sentence-transformers (~80MB download once). No text is generated.

RUN:
    # structural scan only (instant, no model):
    python profile_document.py --pdf "data/doc.pdf"

    # add the chunk-size experiment (downloads a small model first time):
    python profile_document.py --pdf "data/doc.pdf" --experiment
"""

import argparse
import json
import re
import statistics
import sys

import numpy as np
import fitz  # PyMuPDF — text extraction, no model


# ─────────────────────────────────────────────────────────────────────────────
# Load
# ─────────────────────────────────────────────────────────────────────────────
def load_pdf_text(path: str) -> tuple[str, int]:
    doc = fitz.open(path)
    pages = [page.get_text() for page in doc]
    n = doc.page_count
    doc.close()
    return "\n".join(pages), n


def split_sentences(text: str) -> list[str]:
    raw = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [s.strip() for s in raw if len(s.strip()) > 8]


# ─────────────────────────────────────────────────────────────────────────────
# PART A — STRUCTURAL SCAN  (mechanical, no model — these are FACTS)
# ─────────────────────────────────────────────────────────────────────────────
def structural_scan(text: str, page_count: int) -> dict:
    examples      = len(re.findall(r"Example\s+\d+", text))
    currency      = len(re.findall(r"(?:AED|USD|EUR|\$|£|€)\s?[\d,]+", text))
    numeric_lines = len(re.findall(r"\n[^\n]*\d[\d,.\s]+\d[^\n]*\n", text))
    code_fences   = len(re.findall(r"```", text))
    indented      = len(re.findall(r"\n {4,}\S", text))
    article_refs  = len(re.findall(r"Article\s+\d+", text))
    section_refs  = len(re.findall(r"[Ss]ection\s+\d+", text))
    see_refs      = len(re.findall(r"[Ss]ee\s+[Ss]ection|[Rr]efer\s+to", text))
    bullets       = len(re.findall(r"\n\s*[•\-\*]\s", text))

    lines      = [l.strip() for l in text.split("\n") if l.strip()]
    caps_heads = sum(1 for l in lines if l.isupper() and 8 < len(l) < 120)
    num_heads  = sum(1 for l in lines if re.match(r"^\d+\.\d*\s+[A-Z]", l))

    non_ascii = sum(1 for c in text if ord(c) > 127)
    non_ascii_ratio = round(non_ascii / max(len(text), 1), 4)

    return {
        "pages":               page_count,
        "total_chars":         len(text),
        "example_blocks":      examples,
        "currency_figures":    currency,
        "numeric_table_lines": numeric_lines,
        "code_fences":         code_fences,
        "indented_blocks":     indented,
        "article_refs":        article_refs,
        "section_refs":        section_refs,
        "see_refs":            see_refs,
        "bullets":             bullets,
        "caps_headings":       caps_heads,
        "numbered_headings":   num_heads,
        "non_ascii_ratio":     non_ascii_ratio,
    }


def structural_recommendations(p: dict) -> list[tuple[str, str]]:
    """Only structural calls — the things mechanical measurement CAN decide."""
    recs = []

    if p["example_blocks"] >= 5:
        recs.append((
            "Keep worked Example blocks whole (Example-aware splitting)",
            f"{p['example_blocks']} 'Example N' blocks found. Splitting by character "
            f"count would cut setup away from result. Detect and keep each whole."
        ))
    if p["numeric_table_lines"] >= 30 or p["currency_figures"] >= 100:
        recs.append((
            "Handle tables carefully (don't split mid-table)",
            f"{p['numeric_table_lines']} number-heavy lines, {p['currency_figures']} currency "
            f"figures — tables are likely present. Keep rows together."
        ))
    if p["code_fences"] >= 4 or p["indented_blocks"] >= 30:
        recs.append((
            "Split code on logical boundaries (code-aware splitting)",
            "Code signals present. Split on function/block boundaries, not characters."
        ))
    if p["caps_headings"] + p["numbered_headings"] >= 10:
        recs.append((
            "Prepend section headings to chunks",
            f"{p['caps_headings'] + p['numbered_headings']} headings found. Adding the section "
            f"title to each chunk helps embeddings capture topic. (Cheap retrieval boost.)"
        ))
    total_refs = p["article_refs"] + p["section_refs"] + p["see_refs"]
    if total_refs >= 50:
        recs.append((
            "Watch cross-references (add a link layer only if recall suffers)",
            f"{total_refs} cross-references. Small chunks + reranker usually cope. "
            f"Only add a linking layer if your eval shows recall problems."
        ))
    if p["non_ascii_ratio"] > 0.05:
        recs.append((
            "Check the loader — possible OCR or multilingual text",
            f"Non-ASCII ratio {p['non_ascii_ratio']} is elevated. May need an OCR/language-aware loader."
        ))
    else:
        recs.append((
            "Standard text loader is fine (PyMuPDF)",
            f"Non-ASCII ratio {p['non_ascii_ratio']} is low — clean machine-readable text."
        ))
    return recs


# ─────────────────────────────────────────────────────────────────────────────
# PART B — CHUNK-SIZE EXPERIMENT  (measures IDEA cohesion, needs embeddings)
# ─────────────────────────────────────────────────────────────────────────────
def chunk_text(text: str, size: int, overlap: int = 0) -> list[str]:
    chunks, start = [], 0
    step = max(1, size - overlap)
    while start < len(text):
        chunks.append(text[start:start + size])
        start += step
    return [c for c in chunks if c.strip()]


def chunk_cohesion(chunk: str, embed_fn) -> float | None:
    """
    Cohesion = how much the sentences inside a chunk agree with each other.
      high → all sentences about the same idea (chunk holds ONE idea)
      low  → sentences about different things (chunk MIXES ideas)
    Measured as the average pairwise cosine similarity of sentence embeddings.
    Returns None if the chunk has fewer than 2 sentences.
    """
    sents = split_sentences(chunk)
    if len(sents) < 2:
        return None
    vecs = embed_fn(sents)                       # (n, d), normalized
    sims = vecs @ vecs.T                          # cosine similarity matrix
    n = len(sents)
    total = sims.sum() - np.trace(sims)          # exclude self-similarity
    return float(total / (n * (n - 1)))


def run_chunk_experiment(text: str, embed_fn,
                         sizes=(400, 600, 800, 1200, 1600, 2000),
                         sample_n=25) -> dict:
    """For each candidate size, measure average chunk cohesion over a sample."""
    rng = np.random.default_rng(0)
    result = {}
    for size in sizes:
        chunks = chunk_text(text, size, overlap=size // 6)
        if len(chunks) > sample_n:
            idx = rng.choice(len(chunks), sample_n, replace=False)
            sample = [chunks[i] for i in idx]
        else:
            sample = chunks
        cohesions = [c for c in (chunk_cohesion(ch, embed_fn) for ch in sample) if c is not None]
        result[size] = round(statistics.mean(cohesions), 4) if cohesions else None
    return result


def recommend_chunk_size(cohesion_by_size: dict) -> dict:
    """
    The cohesion experiment ONLY works if cohesion actually FALLS as chunk
    size grows — that's the whole theory ("bigger chunks mix more ideas").

    So before recommending anything, we check whether that signal exists:
      - spread:  how much do the numbers move at all?
      - trend:   do the small sizes have HIGHER cohesion than the large ones?

    If there's no real downward trend (the document is too uniform in topic,
    like a tax guide where every page is similar legal language), we REFUSE
    to recommend a size and tell the user to decide by eval instead.
    This prevents the v1/v2 mistake of forcing a confident wrong number.

    Returns a dict: {"status", "size", "reason"}.
    """
    valid = {s: c for s, c in cohesion_by_size.items() if c is not None}
    if len(valid) < 3:
        return {"status": "no_signal", "size": None,
                "reason": "Not enough measurable chunks to judge a trend."}

    sizes  = sorted(valid)
    values = [valid[s] for s in sizes]

    spread = max(values) - min(values)
    early  = statistics.mean(values[:2])     # cohesion at the two SMALLEST sizes
    late   = statistics.mean(values[-2:])    # cohesion at the two LARGEST sizes
    drop   = early - late                    # positive = the signal we want

    # NO SIGNAL: cohesion doesn't fall with size, or barely moves at all.
    if drop < 0.03 or spread < 0.05:
        return {
            "status": "no_signal",
            "size":   None,
            "reason": (
                f"No reliable chunk-size signal. Cohesion does not clearly fall as "
                f"chunks grow (small-size≈{early:.3f}, large-size≈{late:.3f}, "
                f"spread≈{spread:.3f}). This document is too UNIFORM in topic for "
                f"cohesion to separate good chunk sizes from bad — every part uses "
                f"similar language. Decide chunk size with your EVAL SET, not this "
                f"experiment. (Part A's structural advice is still valid.)"
            ),
        }

    # SIGNAL EXISTS: cohesion genuinely falls as chunks grow.
    # Recommend the largest size still within 8% of the tight (small-size) baseline.
    baseline = early
    floor    = baseline * 0.92
    best     = sizes[0]
    for s in sizes:
        if valid[s] >= floor:
            best = s
        else:
            break

    return {
        "status": "signal",
        "size":   best,
        "reason": (
            f"Cohesion clearly falls as chunks grow (small-size≈{early:.3f} → "
            f"large-size≈{late:.3f}). The largest size still within 8% of the tight "
            f"baseline is {best}. Going bigger starts mixing separate ideas."
        ),
    }


def make_local_embedder():
    """Lazy import so Part A works without the model installed."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")  # small, free, local

    def embed_fn(texts: list[str]) -> np.ndarray:
        v = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return np.array(v, dtype=np.float32)
    return embed_fn


# ─────────────────────────────────────────────────────────────────────────────
# Report
# ─────────────────────────────────────────────────────────────────────────────
def print_structural(p: dict, recs: list[tuple[str, str]]):
    print("\n" + "=" * 64)
    print("PART A — STRUCTURAL SCAN  (facts, measured mechanically)")
    print("=" * 64)
    print(f"  Pages:               {p['pages']}")
    print(f"  Total characters:    {p['total_chars']:,}")
    print(f"  Example blocks:      {p['example_blocks']}")
    print(f"  Currency figures:    {p['currency_figures']}")
    print(f"  Numeric/table lines: {p['numeric_table_lines']}")
    print(f"  Code signals:        fences={p['code_fences']}, indented={p['indented_blocks']}")
    print(f"  Cross-references:    articles={p['article_refs']}, sections={p['section_refs']}, see={p['see_refs']}")
    print(f"  Headings:            caps={p['caps_headings']}, numbered={p['numbered_headings']}")
    print(f"  Non-ASCII ratio:     {p['non_ascii_ratio']}")
    print("\n  Structural recommendations:")
    for i, (rec, reason) in enumerate(recs, 1):
        print(f"\n    {i}. {rec}")
        print(f"       → {reason}")


def print_experiment(cohesion: dict, rec: dict):
    print("\n" + "=" * 64)
    print("PART B — CHUNK-SIZE EXPERIMENT  (measured idea cohesion)")
    print("=" * 64)
    print("  Higher cohesion = chunk holds ONE idea. Lower = chunk MIXES ideas.\n")
    print(f"  {'chunk size':>12}   {'cohesion':>9}")
    print(f"  {'-'*12}   {'-'*9}")
    for s in sorted(cohesion):
        c = cohesion[s]
        bar = "█" * int(c * 30) if c else ""
        val = ("%.4f" % c) if c is not None else "n/a"
        print(f"  {s:>12}   {val:>9}  {bar}")

    if rec["status"] == "signal":
        print(f"\n  RECOMMENDED STARTING CHUNK SIZE: {rec['size']}")
        print(f"  → {rec['reason']}")
        print("\n  NOTE: this is EVIDENCE, not a guarantee. Confirm against your eval set.")
    else:
        print(f"\n  ⚠ NO RELIABLE CHUNK-SIZE RECOMMENDATION")
        print(f"  → {rec['reason']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--experiment", action="store_true",
                    help="Also run the chunk-size cohesion experiment (needs embedding model)")
    ap.add_argument("--out", default="profile.json")
    args = ap.parse_args()

    print(f"Profiling: {args.pdf}")
    text, pages = load_pdf_text(args.pdf)

    # PART A — always runs, no model
    scan = structural_scan(text, pages)
    recs = structural_recommendations(scan)
    print_structural(scan, recs)

    output = {"structural": scan, "structural_recommendations": [r for r, _ in recs]}

    # PART B — only if requested
    if args.experiment:
        print("\nRunning chunk-size experiment (loading local embedding model)...")
        try:
            embed_fn = make_local_embedder()
        except ImportError:
            print("  sentence-transformers not installed. Run: pip install sentence-transformers")
            sys.exit(1)
        cohesion = run_chunk_experiment(text, embed_fn)
        rec = recommend_chunk_size(cohesion)
        print_experiment(cohesion, rec)
        output["chunk_cohesion"]          = cohesion
        output["chunk_size_status"]       = rec["status"]
        output["recommended_chunk_size"]  = rec["size"]   # None if no_signal
    else:
        print("\n(Chunk-size experiment skipped. Add --experiment to measure idea cohesion.)")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved profile to {args.out}\n")


if __name__ == "__main__":
    main()