import type { Resource } from "../types";

export default function Resources({ items, title = "Go further" }: { items: Resource[]; title?: string }) {
  if (!items?.length) return null;
  return (
    <div className="resources">
      <div className="fk">{title}</div>
      {items.map((r) => (
        <a key={r.url} className="res" href={r.url} target="_blank" rel="noreferrer">
          <span className={`fmt f-${r.format.toLowerCase()}`}>{r.format}</span>
          <span className="rbody"><b>{r.title}</b><span className="muted">{r.level} · {r.why}</span></span>
        </a>
      ))}
    </div>
  );
}
