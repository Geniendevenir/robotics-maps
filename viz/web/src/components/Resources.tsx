import type { Resource } from "../types";

export function youtubeId(url: string): string | null {
  const m = url.match(/(?:youtube\.com\/(?:watch\?(?:.*&)?v=|embed\/|shorts\/|live\/)|youtu\.be\/)([\w-]{11})/);
  return m ? m[1] : null;
}

export default function Resources({ items, title = "Go further" }: { items: Resource[]; title?: string }) {
  if (!items?.length) return null;
  return (
    <div className="resources">
      <div className="fk">{title}</div>
      {items.map((r) => {
        const yt = youtubeId(r.url);
        return (
          <a key={r.url} className={yt ? "res res-video" : "res"} href={r.url} target="_blank" rel="noreferrer">
            {yt && (
              <span className="thumb">
                <img src={`https://i.ytimg.com/vi/${yt}/mqdefault.jpg`} alt="" loading="lazy" />
                <span className="play">▶</span>
              </span>
            )}
            <span className="rbody">
              <span className="rhead">
                <span className={`fmt f-${r.format.toLowerCase()}`}>{r.format}</span>
                <span className="muted">{r.level}</span>
              </span>
              <b>{r.title}</b>
              <span className="muted">{r.why}</span>
            </span>
          </a>
        );
      })}
    </div>
  );
}
