"""
evaluate_tax.py — LLM-as-judge evaluation for the UAE Tax RAG project.

Adapted from your AI Recruiter evaluate.py — same proven approach:
ONE GPT judge call per question scores all 4 metrics at once.

WHY THIS INSTEAD OF RAGAS:
─────────────────────────────────────────────────────────────────────────
- RAGAS 0.1.21 has dependency conflicts (numpy build, langchain versions)
- RAGAS makes many slow sequential calls per question
- This makes ONE call per question — ~4x faster
- Runs in your main tax-rag environment — only needs openai + openpyxl
- You already proved this approach works on the recruiter project

WHAT IT DOES:
─────────────────────────────────────────────────────────────────────────
Reads the three results JSON files (baseline, ring1, ring2), sends each
question + answer + retrieved context to GPT-4o-mini as a judge, gets back
4 scores, averages them per version, and prints a comparison table.

Unlike the recruiter version, this does NOT re-run the pipeline — it scores
the answers you already generated and saved in the JSON files. Fair
comparison: same answers you already graded by hand.

HOW TO RUN (in your main tax-rag env — NOT ragas-env):
─────────────────────────────────────────────────────────────────────────
    source tax-rag/Scripts/activate
    python evaluate_tax.py
"""

import json
import time
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = OpenAI()

RESULT_FILES = {
    "Baseline": "baseline_results.json",
    "Ring 1":   "ring1_results.json",
    "Ring 2":   "ring2_results.json",
}


# ─────────────────────────────────────────────────────────────────────────────
# GPT-as-judge — one call scores all 4 metrics (same as recruiter project)
# ─────────────────────────────────────────────────────────────────────────────
def score_with_gpt(question: str, answer: str, context: str) -> dict:
    judge_prompt = f"""
You are evaluating a RAG system that answers UAE Corporate Tax questions.
Score the following response on 4 metrics.
Return ONLY a JSON object, nothing else.

Question: {question}

Context retrieved:
{context[:3000]}

Answer given:
{answer[:1500]}

Score each metric from 0.0 to 1.0:

{{
  "faithfulness": <did the answer use ONLY the context, no made-up facts or numbers? 1.0=fully grounded, 0.0=hallucinated>,
  "answer_relevancy": <did the answer address the question asked? 1.0=fully on-topic, 0.0=off-topic>,
  "context_precision": <were the retrieved chunks relevant to the question? 1.0=all useful, 0.0=mostly noise>,
  "context_recall": <did the context contain enough info to fully answer? 1.0=complete, 0.0=key info missing>
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": judge_prompt}],
        temperature=0,
    )
    raw = response.choices[0].message.content.strip()
    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception:
        return {
            "faithfulness": 0.0,
            "answer_relevancy": 0.0,
            "context_precision": 0.0,
            "context_recall": 0.0,
        }


# ─────────────────────────────────────────────────────────────────────────────
# Pull context text from a result record (handles all 3 formats)
# ─────────────────────────────────────────────────────────────────────────────
def get_context(record: dict) -> str:
    # Ring 2 has "compressed", Ring 1 + Baseline have "retrieved"
    if record.get("compressed"):
        chunks = record["compressed"]
    elif record.get("retrieved"):
        chunks = record["retrieved"]
    else:
        return ""
    return "\n\n".join(c.get("text", "") for c in chunks)


# ─────────────────────────────────────────────────────────────────────────────
# Score one version's results
# ─────────────────────────────────────────────────────────────────────────────
def evaluate_version(name: str, path: str) -> dict:
    print(f"\n{'=' * 55}")
    print(f"Scoring: {name}  ({path})")
    print("=" * 55)

    with open(path, encoding="utf-8") as f:
        results = json.load(f)

    scored = []
    for i, r in enumerate(results, 1):
        question = r["question"]
        answer   = r["answer"]
        context  = get_context(r)

        s = score_with_gpt(question, answer, context)
        scored.append(s)

        print(f"  [{i}/{len(results)}] Q{r['num']:<2} "
              f"faith={s['faithfulness']:.2f} "
              f"rel={s['answer_relevancy']:.2f} "
              f"prec={s['context_precision']:.2f} "
              f"rec={s['context_recall']:.2f}")
        time.sleep(0.3)   # gentle on rate limits

    n = len(scored)
    return {
        "faithfulness":      sum(s["faithfulness"]      for s in scored) / n,
        "answer_relevancy":  sum(s["answer_relevancy"]  for s in scored) / n,
        "context_precision": sum(s["context_precision"] for s in scored) / n,
        "context_recall":    sum(s["context_recall"]    for s in scored) / n,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────
def main():
    all_scores = {}
    for name, path in RESULT_FILES.items():
        try:
            all_scores[name] = evaluate_version(name, path)
        except FileNotFoundError:
            print(f"  SKIPPED — {path} not found")

    # ── Comparison table ──
    print("\n\n" + "=" * 70)
    print("FINAL COMPARISON — UAE Tax RAG")
    print("=" * 70)

    metrics = ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]
    header = f"{'Metric':<20}" + "".join(f"{name:>14}" for name in all_scores)
    print(header)
    print("-" * 70)

    for m in metrics:
        row = f"{m:<20}"
        for name in all_scores:
            row += f"{all_scores[name][m]:>14.3f}"
        print(row)

    # Overall row
    print("-" * 70)
    overall_row = f"{'OVERALL':<20}"
    for name in all_scores:
        overall = sum(all_scores[name].values()) / len(metrics)
        overall_row += f"{overall:>14.3f}"
    print(overall_row)
    print("=" * 70)

    # Save
    report = {
        name: {**scores, "overall": sum(scores.values()) / len(metrics)}
        for name, scores in all_scores.items()
    }
    with open("eval_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("\nSaved to eval_report.json — bring it back and we'll read it together.")


if __name__ == "__main__":
    main()