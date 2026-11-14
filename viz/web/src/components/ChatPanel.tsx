import { useEffect, useRef, useState } from "react";
import { useStore } from "../store";
import { api, streamChat } from "../api";
import { nodeMatches } from "../filters";

const SUGGESTIONS = [
  "Give me a quick recap of what I'm looking at",
  "Suggest a 3-step path for a team strong in AI but weak in electronics",
  "Group the cheapest Robot learning projects at Level 2 or below",
  "Which Paris organizations could host or sponsor a hackathon?",
];

function render(text: string) {
  return text.split("\n").map((line, i) => <p key={i}>{line.split(/(\*\*[^*]+\*\*)/g).map((s, j) => s.startsWith("**") ? <b key={j}>{s.slice(2, -2)}</b> : s)}</p>);
}

export default function ChatPanel() {
  const { chat, view, selectedId, filters, data, groups } = useStore();
  const setChat = useStore((s) => s.setChat);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [status, setStatus] = useState<{ backend: string; model?: string } | null>(null);
  const abort = useRef<AbortController | null>(null);
  const end = useRef<HTMLDivElement>(null);
  useEffect(() => { api.chatStatus().then(setStatus).catch(() => setStatus({ backend: "none" })); }, []);
  useEffect(() => { end.current?.scrollIntoView({ behavior: "smooth" }); }, [chat]);

  const send = async (text: string) => {
    if (!text.trim() || busy) return;
    const msgs = [...chat, { role: "user" as const, content: text.trim() }];
    setChat(() => [...msgs, { role: "assistant", content: "", tools: [] }]);
    setInput("");
    setBusy(true);
    abort.current = new AbortController();
    const visible = (data?.nodes ?? []).filter((n) => nodeMatches(n, filters[view], groups, view === "graph") && (view === "graph" || n.type === "org")).length;
    const upd = (fn: (m: any) => void) => setChat((c) => { const copy = c.slice(); const last = { ...copy[copy.length - 1], tools: [...(copy[copy.length - 1].tools ?? [])] }; fn(last); copy[copy.length - 1] = last; return copy; });
    try {
      await streamChat(msgs, { view, selected_node_id: selectedId, filters: filters[view], visible_node_ids_count: visible }, (e) => {
        if (e.type === "text") upd((m) => { m.content += e.text; });
        else if (e.type === "tool") upd((m) => { m.tools.push({ name: e.name, input: e.input, result_summary: e.result_summary }); });
        else if (e.type === "error") upd((m) => { m.content += `\n⚠ ${e.message}`; });
      }, abort.current.signal);
    } catch (err) {
      upd((m) => { m.content += `\n⚠ ${String(err)}`; });
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="chat">
      <div className="chat-status muted small">
        Guide: {status ? (status.backend === "none" ? "not configured — see README (MCP from Claude Desktop/Code still works)" : `${status.backend}${status.model ? ` · ${status.model}` : ""}`) : "…"}
      </div>
      <div className="msgs">
        {chat.length === 0 && (
          <div className="suggest">
            <div className="muted">Ask the guide to explain, recap, compare or build groups. It sees the current view and selection.</div>
            {SUGGESTIONS.map((s) => <button key={s} onClick={() => send(s)}>{s}</button>)}
          </div>
        )}
        {chat.map((m, i) => (
          <div key={i} className={"msg " + m.role}>
            {m.tools && m.tools.length > 0 && (
              <div className="tools">{m.tools.map((t, j) => <span key={j} className="tool" title={JSON.stringify(t.input)}>⚙ {t.name}{t.result_summary ? ` · ${t.result_summary}` : ""}</span>)}</div>
            )}
            {m.content ? render(m.content) : (busy && i === chat.length - 1 ? <span className="typing">thinking…</span> : null)}
          </div>
        ))}
        <div ref={end} />
      </div>
      <div className="chat-input">
        <textarea rows={2} placeholder="Ask the guide…" value={input} onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(input); } }} />
        {busy ? <button onClick={() => abort.current?.abort()}>Stop</button> : <button onClick={() => send(input)}>Send</button>}
        {chat.length > 0 && !busy && <button className="link" onClick={() => setChat(() => [])}>clear</button>}
      </div>
    </div>
  );
}
