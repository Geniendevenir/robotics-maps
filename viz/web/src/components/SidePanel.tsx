import { useState } from "react";
import { useStore } from "../store";
import { api } from "../api";
import { arr, isOpen, str } from "../filters";
import { branchColor, GROUP_COLORS, TYPE_LABELS } from "../colors";
import type { MapNode } from "../types";

const linkify = (s: string) =>
  s.split(/(https?:\/\/[^\s<>"')\]]+)/g).map((part, i) =>
    /^https?:\/\//.test(part) ? <a key={i} href={part} target="_blank" rel="noreferrer">{part.replace(/^https?:\/\/(www\.)?/, "").slice(0, 60)}</a> : part);

function Field({ k, v }: { k: string; v: unknown }) {
  const s = Array.isArray(v) ? v.join(", ") : typeof v === "boolean" ? (v ? "Yes" : "No") : str(v);
  if (!s || s === "unknown" || s === "N/A") return null;
  return <div className="field"><div className="fk">{k}</div><div className="fv">{linkify(s)}</div></div>;
}

function Bar({ label, v, color }: { label: string; v: number; color: string }) {
  return <div className="bar"><span>{label}</span><div><i style={{ width: `${v}%`, background: color }} /></div><b>{v}%</b></div>;
}

function Axis({ label, v }: { label: string; v: unknown }) {
  const s = str(v);
  if (!s) return null;
  const n = parseInt(s, 10);
  return <div className="axis"><span>{label}</span><div className="dots">{[1, 2, 3, 4, 5].map((i) => <i key={i} className={i <= n ? "on" : ""} />)}</div><em>{s.replace(/^\d\s*-\s*/, "")}</em></div>;
}

const SECTIONS: Record<MapNode["type"], { hero: string[]; facts: string[]; more: string[] }> = {
  project: { hero: ["Description", "Deliverable"], facts: ["Duration", "Hardware cost", "Wow factor", "Kind", "Secondary branches", "Status"], more: ["References"] },
  knowledge: { hero: ["What it is"], facts: ["Accessibility for us", "Starter hardware cost", "Time to first demo", "Discipline", "Prerequisites"], more: ["Frontier state 2026", "Key players", "Best resources", "Sources"] },
  robot: { hero: ["Why it matters"], facts: ["Kind", "Form factor", "Model type", "Release year", "Open source", "Price / access", "Builder (if not in map)"], more: ["Key specs", "Sources"] },
  org: { hero: ["What they build"], facts: ["Type", "Region", "City", "Size / stage", "Value chain", "Sector", "Open source", "Relationship potential"], more: ["Warm contact path", "Website", "Sources"] },
};

const REL_LABELS: Record<string, [string, string]> = {
  prerequisite: ["Unlocks", "Prerequisites"],
  "project-knowledge": ["Knowledge", "Used in projects"],
  "project-robot": ["Robots & models", "Used in projects"],
  "project-org": ["Relevant orgs", "Projects"],
  "robot-knowledge": ["Knowledge", "Robots & models"],
  "robot-builder": ["Built by", "Builds"],
  "robot-user": ["Used by", "Uses"],
};

export function NodeChip({ id }: { id: string }) {
  const n = useStore((s) => s.index?.byId.get(id));
  const select = useStore((s) => s.select);
  const branches = useStore((s) => s.index?.branches ?? []);
  if (!n) return <span className="nchip missing">{id}</span>;
  return (
    <button className={`nchip t-${n.type}`} onClick={() => select(id, { focus: true })} title={TYPE_LABELS[n.type]}>
      {n.image ? <img src={n.image} alt="" /> : <i style={{ background: branchColor(n.branch, branches) }} />}
      {n.name}
    </button>
  );
}

function GroupAdd({ ids }: { ids: string[] }) {
  const groups = useStore((s) => s.groups);
  const [name, setName] = useState("");
  return (
    <div className="gadd">
      <select value="" onChange={async (e) => { if (e.target.value) await api.addToGroup(e.target.value, ids); }}>
        <option value="">+ Add {ids.length > 1 ? `${ids.length} nodes` : ""} to group…</option>
        {groups.map((g) => <option key={g.id} value={g.id}>{g.name} ({g.node_ids.length})</option>)}
      </select>
      <input placeholder="or new group name" value={name} onChange={(e) => setName(e.target.value)}
        onKeyDown={async (e) => {
          if (e.key === "Enter" && name.trim()) {
            await api.createGroup({ name: name.trim(), node_ids: ids, color: GROUP_COLORS[groups.length % GROUP_COLORS.length] });
            setName("");
          }
        }} />
    </div>
  );
}

export default function SidePanel() {
  const { index, selectedId, multi, groups } = useStore();
  const n = selectedId ? index?.byId.get(selectedId) : undefined;
  if (multi.length > 1) {
    return (
      <div className="details">
        <h2>{multi.length} nodes selected</h2>
        <GroupAdd ids={multi} />
        <div className="chiplist">{multi.slice(0, 80).map((id) => <NodeChip key={id} id={id} />)}</div>
      </div>
    );
  }
  if (!n || !index) return <div className="details empty">Click a node to see its essentials. Shift-drag on the whiteboard to select several and add them to a group.</div>;
  const F = n.fields;
  const sec = SECTIONS[n.type];
  const rels = new Map<string, string[]>();
  for (const e of index.adj.get(n.id) ?? []) {
    const [outL, inL] = REL_LABELS[e.kind] ?? [e.kind, e.kind];
    const label = e.dir === "out" ? outL : inL;
    if (!rels.has(label)) rels.set(label, []);
    rels.get(label)!.push(e.id);
  }
  const inGroups = groups.filter((g) => g.node_ids.includes(n.id));
  const color = branchColor(n.branch, index.branches);
  const sw = +str(F["Software %"]) || 0, me = +str(F["Mechanical %"]) || 0, el = +str(F["Electrical %"]) || 0;
  return (
    <div className="details">
      <div className="dhead">
        {n.image && <img className="hero-img" src={n.image} alt="" />}
        <div>
          <div className="dtype">{TYPE_LABELS[n.type]}{n.branch && <span className="badge" style={{ background: color }}>{n.branch}</span>}
            {n.type === "project" && <span className="badge lvl">Level {n.level}</span>}
            {n.type === "knowledge" && n.level && <span className="badge lvl">{String(n.level)}</span>}
            {n.type === "org" && n.geo?.approx && <span className="badge warn">approx. location</span>}
          </div>
          <h2>{n.name}</h2>
          <div className="dlinks">
            {n.notion_url && <a href={n.notion_url} target="_blank" rel="noreferrer">Open in Notion ↗</a>}
            {n.type === "org" && str(F["Website"]) && <a href={str(F["Website"])} target="_blank" rel="noreferrer">Website ↗</a>}
          </div>
        </div>
      </div>
      {sec.hero.map((k) => str(F[k]) && <p key={k} className="hero"><b>{k === "Deliverable" ? "Deliverable: " : ""}</b>{linkify(str(F[k]))}</p>)}
      {n.type === "project" && (
        <div className="scores">
          <Axis label="Novelty" v={F["Novelty"]} /><Axis label="Autonomy" v={F["Autonomy"]} />
          <Axis label="Hardware" v={F["Hardware"]} /><Axis label="Integration" v={F["Integration"]} />
          {(sw || me || el) ? <div className="mix"><Bar label="Software" v={sw} color="#4dabf7" /><Bar label="Mechanical" v={me} color="#ffa94d" /><Bar label="Electrical" v={el} color="#ffd43b" /></div> : null}
        </div>
      )}
      <div className="facts">{sec.facts.map((k) => <Field key={k} k={k} v={k === "Open source" ? (F[k] == null ? null : isOpen(F[k])) : F[k]} />)}</div>
      {[...rels.entries()].map(([label, ids]) => (
        <div key={label} className="rel">
          <div className="fk">{label} ({ids.length})</div>
          <div className="chiplist">{ids.slice(0, 40).map((id) => <NodeChip key={id} id={id} />)}{ids.length > 40 && <span className="muted">+{ids.length - 40} more</span>}</div>
        </div>
      ))}
      <div className="groups-of">
        {inGroups.map((g) => <span key={g.id} className="gtag" style={{ borderColor: g.color }}>{g.name}
          <button className="link" onClick={() => api.removeFromGroup(g.id, [n.id])}>×</button></span>)}
      </div>
      <GroupAdd ids={[n.id]} />
      <details className="more"><summary>More details</summary>
        {sec.more.map((k) => <Field key={k} k={k} v={F[k]} />)}
        {Object.entries(F).filter(([k]) => ![...sec.hero, ...sec.facts, ...sec.more, "Software %", "Mechanical %", "Electrical %", "Novelty", "Autonomy", "Hardware", "Integration", "Branch", "Level"].includes(k))
          .map(([k, v]) => <Field key={k} k={k} v={v} />)}
      </details>
    </div>
  );
}
export { arr };
