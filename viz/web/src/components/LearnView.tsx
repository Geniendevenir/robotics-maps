import { useStore } from "../store";
import { branchColor } from "../colors";
import Markdown from "./Markdown";
import Resources from "./Resources";
import { NodeChip } from "./SidePanel";

export default function LearnView() {
  const { data, index, chapterId, setChapter } = useStore();
  const guide = data?.guide;
  if (!guide || !index) return <div className="loading">No guide yet. Build it into output/lessons/guide.json and rerun viz/scripts/build_data.py.</div>;
  const chapter = guide.chapters.find((c) => c.id === chapterId);
  const pos = chapter ? guide.chapters.indexOf(chapter) : -1;
  const next = guide.chapters[pos + 1];
  const prev = pos > 0 ? guide.chapters[pos - 1] : null;
  const lessonsIn = (branch: string | null) => data!.nodes.filter((n) => n.lesson && (branch === null ? n.type === "org" : n.branch === branch)).length;
  return (
    <div className="learn">
      <nav className="toc">
        <div className="toc-title">{guide.title}</div>
        <button className={chapterId === "intro" ? "on" : ""} onClick={() => setChapter("intro")}><span className="num">0</span>Start here</button>
        {guide.chapters.map((c, i) => (
          <button key={c.id} className={c.id === chapterId ? "on" : ""} onClick={() => setChapter(c.id)}>
            <span className="num" style={{ background: c.branch ? branchColor(c.branch, index.branches) : undefined }}>{i + 1}</span>
            {c.title.split(":")[0]}
          </button>
        ))}
      </nav>
      <article className="reader">
        {!chapter ? (
          <>
            <h1>{guide.title}</h1>
            <Markdown text={guide.intro_md} />
            {guide.chapters[0] && <button className="primary" onClick={() => setChapter(guide.chapters[0].id)}>Start chapter 1: {guide.chapters[0].title} →</button>}
          </>
        ) : (
          <>
            <div className="chapter-kicker">Chapter {pos + 1}{chapter.branch && <span className="badge" style={{ background: branchColor(chapter.branch, index.branches) }}>{chapter.branch}</span>}</div>
            <h1>{chapter.title}</h1>
            <Markdown text={chapter.body_md} />
            <div className="start-here">
              <div className="fk">Start here: click a node to read its beginner explanation</div>
              <div className="chiplist">{chapter.start_here.map((id) => <NodeChip key={id} id={id} />)}</div>
              <div className="muted small">{lessonsIn(chapter.branch)} nodes in this {chapter.branch ? "branch" : "chapter"} have a beginner explanation so far.</div>
            </div>
            <Resources items={chapter.resources} title="Learn more about this field" />
            <div className="pager">
              <button onClick={() => setChapter(prev ? prev.id : "intro")}>← {prev ? prev.title.split(":")[0] : "Start here"}</button>
              {next && <button className="primary" onClick={() => setChapter(next.id)}>{next.title.split(":")[0]} →</button>}
            </div>
          </>
        )}
      </article>
    </div>
  );
}
