import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/ask";

const EXAMPLES = [
  "What is the corporate tax rate in the UAE?",
  "Do I have to register if my profit is below the threshold?",
  "I freelance from home with no trade licence — do I owe corporate tax?",
  "What records must I keep, and for how long?",
];

export default function App() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [openChunks, setOpenChunks] = useState(false);

  async function ask(q) {
    const query = (q ?? question).trim();
    if (!query) return;
    setLoading(true);
    setError("");
    setResult(null);
    setOpenChunks(false);
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: query }),
      });
      const data = await res.json();
      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
      }
    } catch {
      setError(
        "Can't reach the assistant. Make sure the API is running on port 8000 (uvicorn api:app --port 8000)."
      );
    } finally {
      setLoading(false);
    }
  }

  function onExample(ex) {
    setQuestion(ex);
    ask(ex);
  }

  return (
    <div className="page">
      <header className="masthead">
        <div className="crest" aria-hidden="true">★</div>
        <div className="masthead-text">
          <h1>UAE Corporate Tax Guide</h1>
          <p>
            Answers grounded in the Federal Tax Authority's official
            Corporate Tax General Guide (CTGGCT1, September 2023).
          </p>
        </div>
      </header>
      <div className="gold-rule" />

      <main className="content">
        <section className="ask-block">
          <label className="ask-label" htmlFor="q">
            Ask a question about UAE Corporate Tax
          </label>
          <div className="ask-row">
            <input
              id="q"
              className="ask-input"
              type="text"
              placeholder="e.g. What is the corporate tax rate?"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && ask()}
            />
            <button className="ask-button" onClick={() => ask()} disabled={loading}>
              {loading ? "Consulting…" : "Ask"}
            </button>
          </div>

          <div className="examples">
            {EXAMPLES.map((ex) => (
              <button key={ex} className="chip" onClick={() => onExample(ex)}>
                {ex}
              </button>
            ))}
          </div>
        </section>

        {loading && (
          <div className="status">Consulting the official guide…</div>
        )}

        {error && <div className="error">{error}</div>}

        {result && (
          <section className="answer-block">
            <div className="answer-text">{result.answer}</div>

            {result.citations?.length > 0 && (
              <div className="citations">
                <span className="citations-label">Sources</span>
                {result.citations.map((p) => (
                  <span key={p} className="citation">CTGGCT1 · p.{p}</span>
                ))}
              </div>
            )}

            {result.chunks?.length > 0 && (
              <div className="sources">
                <button
                  className="sources-toggle"
                  onClick={() => setOpenChunks((v) => !v)}
                >
                  {openChunks ? "Hide source passages" : "View source passages"}
                </button>
                {openChunks && (
                  <ol className="source-list">
                    {result.chunks.map((c) => (
                      <li key={c.rank} className="source-item">
                        <div className="source-meta">
                          <span className="source-page">Page {c.page}</span>
                          <span className="source-score">relevance {c.score}</span>
                        </div>
                        <p className="source-snippet">{c.text}</p>
                      </li>
                    ))}
                  </ol>
                )}
              </div>
            )}
          </section>
        )}
      </main>

      <footer className="disclaimer">
        Informational only — not tax advice. Answers are drawn solely from the
        FTA Corporate Tax General Guide and may not reflect later amendments.
        Confirm with a qualified tax professional before acting.
      </footer>
    </div>
  );
}