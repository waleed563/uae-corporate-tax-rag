"""
check_chunks.py — Measure whether your chunker produced GOOD chunks.

Your course taught you to print chunks and eyeball them, plus measure
count / avg / min / max length. That tells you the chunker RAN. It does
NOT tell you the chunks are GOOD — a splitter can make perfectly even
chunks that all slice through the middle of rules.

This tool turns eyeballing into MEASUREMENT. No LLM — pure string checks.
It reuses the idea from profile_document.py Part A: that scan told us what
to PROTECT (Example blocks, tables); this checks whether the chunker did.

Point it at ANY chunker via settings (--chunk-size, --chunk-overlap, --splitter).

FOUR QUALITY SIGNALS IT MEASURES:
─────────────────────────────────────────────────────────────────────────
1. BOUNDARY DAMAGE — what % of chunks start/end mid-sentence?
   A good chunk ends on a sentence boundary. Many chunks starting with a
   lowercase letter (mid-sentence) means the splitter is cutting through ideas.

2. EXAMPLE INTEGRITY — how many "Example N" blocks got their header
   separated from their content? Part A found 36 Examples to keep whole.
   This checks how many survived chunking intact.

3. ORPHAN CHUNKS — how many tiny fragment chunks (< 100 chars)?
   These are scraps from bad splits that pollute retrieval.

4. LENGTH CONSISTENCY — not just the average, but the SPREAD.
   Wildly uneven chunk lengths signal the splitter is fighting the document.

It does NOT produce a single fake "score". It reports each signal with a
transparent GOOD / WATCH / BAD flag and lets you judge. Thresholds are
printed so you can see exactly why each flag was raised.

RUN:
    python check_chunks.py --pdf "data/doc.pdf" --chunk-size 600 --chunk-overlap 100
    python check_chunks.py --pdf "data/doc.pdf" --chunk-size 2000 --splitter recursive
"""

import argparse
import json
import re
import statistics
import sys

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
)

ORPHAN_MAX_CHARS = 100   # chunks shorter than this are "orphan" fragments


# ─────────────────────────────────────────────────────────────────────────────
# Build the chunker from settings (point it at anything)
# ─────────────────────────────────────────────────────────────────────────────
def build_splitter(name: str, size: int, overlap: int):
    if name == "recursive":
        return RecursiveCharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap,
            separators=["\n\n", "\n", ". ", " ", ""],
        )
    if name == "character":
        return CharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap, separator="\n\n",
        )
    if name == "token":
        return TokenTextSplitter(chunk_size=size, chunk_overlap=overlap)
    raise ValueError(f"Unknown splitter: {name}")


# ─────────────────────────────────────────────────────────────────────────────
# Signal 1 — boundary damage
# ─────────────────────────────────────────────────────────────────────────────
def boundary_damage(chunks: list[str]) -> dict:
    """A clean chunk starts with a capital/number/bullet and ends with
    sentence punctuation. Mid-sentence starts/ends = the splitter cut an idea."""
    clean_start = 0
    clean_end   = 0
    for c in chunks:
        c = c.strip()
        if not c:
            continue
        first = c[0]
        last  = c[-1]
        # clean start: uppercase, digit, opening bracket/quote, or bullet
        if first.isupper() or first.isdigit() or first in '(["“•-':
            clean_start += 1
        # clean end: sentence-ending punctuation
        if last in '.!?:;)"”':
            clean_end += 1
    n = len(chunks)
    return {
        "clean_start_pct": round(100 * clean_start / n, 1),
        "clean_end_pct":   round(100 * clean_end / n, 1),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Signal 2 — example integrity
# ─────────────────────────────────────────────────────────────────────────────
def example_integrity(full_text: str, chunks: list[str]) -> dict:
    """
    Count 'Example N' headers in the source. Then count how many landed in a
    chunk with enough content AFTER them (>= 120 chars) to be usable.
    A header stranded at the end of a chunk = its body got split off.
    Heuristic, but directly measures what Part A told us to protect.
    """
    total_examples = len(re.findall(r"Example\s+\d+", full_text))
    if total_examples == 0:
        return {"total": 0, "intact": 0, "intact_pct": 100.0}

    intact = 0
    for c in chunks:
        for m in re.finditer(r"Example\s+\d+", c):
            content_after = len(c) - m.end()
            if content_after >= 120:        # header has its body attached
                intact += 1
    # cap at total (overlap can double-count)
    intact = min(intact, total_examples)
    return {
        "total":      total_examples,
        "intact":     intact,
        "intact_pct": round(100 * intact / total_examples, 1),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Signal 3 — orphan chunks
# ─────────────────────────────────────────────────────────────────────────────
def orphan_chunks(chunks: list[str]) -> dict:
    orphans = [c for c in chunks if len(c.strip()) < ORPHAN_MAX_CHARS]
    return {
        "orphan_count": len(orphans),
        "orphan_pct":   round(100 * len(orphans) / len(chunks), 1),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Signal 4 — length distribution
# ─────────────────────────────────────────────────────────────────────────────
def length_distribution(chunks: list[str]) -> dict:
    lens = [len(c) for c in chunks]
    mean = statistics.mean(lens)
    std  = statistics.pstdev(lens)
    return {
        "count":  len(chunks),
        "avg":    round(mean),
        "median": round(statistics.median(lens)),
        "min":    min(lens),
        "max":    max(lens),
        "std":    round(std),
        "cv":     round(std / mean, 2) if mean else 0,   # coefficient of variation
    }


# ─────────────────────────────────────────────────────────────────────────────
# Flagging — transparent thresholds, no hidden magic, no fake composite score
# ─────────────────────────────────────────────────────────────────────────────
def flag(value, good, watch, higher_is_better=True):
    if higher_is_better:
        if value >= good:  return "GOOD "
        if value >= watch: return "WATCH"
        return "BAD  "
    else:
        if value <= good:  return "GOOD "
        if value <= watch: return "WATCH"
        return "BAD  "


def print_report(cfg, dist, bound, examples, orphans):
    print("\n" + "=" * 66)
    print(f"CHUNK QUALITY — {cfg['splitter']}, size={cfg['chunk_size']}, overlap={cfg['chunk_overlap']}")
    print("=" * 66)

    print("\n  LENGTH DISTRIBUTION")
    print(f"    chunks={dist['count']}  avg={dist['avg']}  median={dist['median']}  "
          f"min={dist['min']}  max={dist['max']}")
    cv_flag = flag(dist["cv"], 0.3, 0.5, higher_is_better=False)
    print(f"    consistency (CV={dist['cv']}): [{cv_flag}]   "
          f"(GOOD<=0.30, WATCH<=0.50 — lower = more even chunks)")

    print("\n  BOUNDARY DAMAGE  (are chunks cut mid-sentence?)")
    s_flag = flag(bound["clean_start_pct"], 85, 70)
    e_flag = flag(bound["clean_end_pct"],   85, 70)
    print(f"    clean starts: {bound['clean_start_pct']}%  [{s_flag}]  (GOOD>=85%)")
    print(f"    clean ends:   {bound['clean_end_pct']}%  [{e_flag}]  (GOOD>=85%)")

    print("\n  EXAMPLE INTEGRITY  (did 'Example N' blocks stay whole?)")
    if examples["total"] == 0:
        print("    no Example blocks in this document — n/a")
    else:
        x_flag = flag(examples["intact_pct"], 90, 75)
        print(f"    {examples['intact']}/{examples['total']} intact "
              f"({examples['intact_pct']}%)  [{x_flag}]  (GOOD>=90%)")

    print("\n  ORPHAN CHUNKS  (tiny <100-char fragments)")
    o_flag = flag(orphans["orphan_pct"], 2, 5, higher_is_better=False)
    print(f"    {orphans['orphan_count']} orphans ({orphans['orphan_pct']}%)  "
          f"[{o_flag}]  (GOOD<=2%)")

    print("\n  HOW TO READ THIS:")
    print("    These are mechanical signals, not a verdict. A WATCH/BAD flag")
    print("    means 'look here', not 'this chunker failed'. The final word on")
    print("    chunk quality is still your retrieval eval. Use this to catch")
    print("    obvious damage (cut sentences, split Examples) BEFORE you embed.")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--chunk-size", type=int, default=600)
    ap.add_argument("--chunk-overlap", type=int, default=100)
    ap.add_argument("--splitter", default="recursive",
                    choices=["recursive", "character", "token"])
    ap.add_argument("--out", default="chunk_quality.json")
    args = ap.parse_args()

    print(f"Loading: {args.pdf}")
    pages     = PyMuPDFLoader(args.pdf).load()
    full_text = "\n".join(p.page_content for p in pages)

    splitter = build_splitter(args.splitter, args.chunk_size, args.chunk_overlap)
    docs     = splitter.split_documents(pages)
    chunks   = [d.page_content for d in docs if d.page_content.strip()]
    if not chunks:
        sys.exit("No chunks produced.")

    cfg      = {"splitter": args.splitter,
                "chunk_size": args.chunk_size,
                "chunk_overlap": args.chunk_overlap}
    dist     = length_distribution(chunks)
    bound    = boundary_damage(chunks)
    examples = example_integrity(full_text, chunks)
    orphans  = orphan_chunks(chunks)

    print_report(cfg, dist, bound, examples, orphans)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"config": cfg, "length": dist, "boundary": bound,
                   "examples": examples, "orphans": orphans}, f, indent=2)
    print(f"Saved to {args.out}\n")


if __name__ == "__main__":
    main()