import { useMemo } from "react";
import { useStore } from "../store";
import { optionValues } from "../filters";
import { branchColor, TYPE_LABELS } from "../colors";
import type { Filters, NodeType } from "../types";

function Chips({ label, options, value, onChange, color }: {
  label: string; options: string[]; value?: string[]; onChange: (v: string[]) => void; color?: (o: string) => string;
}) {
  if (!options.length) return null;
  const set = new Set(value ?? []);
  return (
    <div className="fgroup">
      <div className="flabel">
        {label}
        {set.size > 0 && <button className="link" onClick={() => onChange([])}>clear</button>}
      </div>
      <div className="chips">
        {options.map((o) => (
          <button key={o} className={"chip" + (set.has(o) ? " on" : "")}
            style={color ? { borderColor: color(o) } : undefined}
            onClick={() => { const s = new Set(set); s.has(o) ? s.delete(o) : s.add(o); onChange([...s]); }}>
            {color && <i style={{ background: color(o) }} />}{o}
          </button>
        ))}
      </div>
    </div>
  );
}

export default function FilterPanel() {
  const { data, index, view, filters, groups, showAllEdges, hideIsolated } = useStore();
  const patch = useStore((s) => s.patchFilters);
  const setFilters = useStore((s) => s.setFilters);
  const setShowAllEdges = useStore((s) => s.setShowAllEdges);
  const setHideIsolated = useStore((s) => s.setHideIsolated);
  const f = filters[view];
  const p = (x: Partial<Filters>) => patch(view, x);
  const nodes = data?.nodes ?? [];
  const opts = useMemo(() => ({
    projectKind: optionValues(nodes, "project", "Kind"),
    hwCost: optionValues(nodes, "project", "Hardware cost"),
    kLevel: ["Fundamental", "Applied", "Frontier"],
    robotKind: optionValues(nodes, "robot", "Kind"),
    orgType: optionValues(nodes, "org", "Type"),
    region: optionValues(nodes, "org", "Region"),
    valueChain: optionValues(nodes, "org", "Value chain"),
    sector: optionValues(nodes, "org", "Sector"),
    rel: optionValues(nodes, "org", "Relationship potential"),
  }), [nodes]);
  const types = f.types ?? [];
  const showType = (t: NodeType) => view === "map" ? t === "org" : types.length === 0 || types.includes(t);
  const counts = useMemo(() => {
    const c: Record<string, number> = {};
    for (const n of nodes) c[n.type] = (c[n.type] ?? 0) + 1;
    return c;
  }, [nodes]);

  return (
    <div className="filters">
      <input className="search" placeholder="Search names and descriptions…" value={f.search ?? ""}
        onChange={(e) => p({ search: e.target.value })} />
      {f.group_id && (
        <div className="active-group">
          Showing group <b>{groups.find((g) => g.id === f.group_id)?.name ?? f.group_id}</b>
          <button className="link" onClick={() => p({ group_id: null })}>show all</button>
        </div>
      )}
      {view === "graph" && (
        <Chips label="Show" options={["project", "knowledge", "robot", "org"]}
          value={types} onChange={(v) => p({ types: v as NodeType[] })}
          color={(o) => ({ project: "#f8f9fa", knowledge: "#ffd43b", robot: "#4dabf7", org: "#b197fc" }[o]!)} />
      )}
      {view === "graph" && (
        <div className="muted small">{(["project", "knowledge", "robot", "org"] as NodeType[]).map((t) => `${TYPE_LABELS[t]} ${counts[t] ?? 0}`).join(" · ")}</div>
      )}
      {view === "graph" && (
        <Chips label="Branch" options={index?.branches ?? []} value={f.branches}
          onChange={(v) => p({ branches: v })} color={(o) => branchColor(o, index?.branches ?? [])} />
      )}
      {view === "graph" && showType("project") && (
        <>
          <div className="fgroup">
            <div className="flabel">Project level {(f.level_min ?? 0).toFixed(2).replace(/\.?0+$/, "")} – {(f.level_max ?? 5).toFixed(2).replace(/\.?0+$/, "")}</div>
            <div className="range">
              <input type="range" min={0} max={5} step={1 / 3} value={f.level_min ?? 0} onChange={(e) => p({ level_min: +e.target.value || null })} />
              <input type="range" min={0} max={5} step={1 / 3} value={f.level_max ?? 5} onChange={(e) => p({ level_max: +e.target.value >= 5 ? null : +e.target.value })} />
            </div>
          </div>
          <Chips label="Project kind" options={opts.projectKind} value={f.project_kind} onChange={(v) => p({ project_kind: v })} />
          <Chips label="Hardware cost" options={opts.hwCost} value={f.hardware_cost} onChange={(v) => p({ hardware_cost: v })} />
        </>
      )}
      {view === "graph" && showType("knowledge") && (
        <Chips label="Knowledge level" options={opts.kLevel} value={f.knowledge_level} onChange={(v) => p({ knowledge_level: v })} />
      )}
      {view === "graph" && showType("robot") && (
        <Chips label="Robot / model kind" options={opts.robotKind} value={f.robot_kind} onChange={(v) => p({ robot_kind: v })} />
      )}
      {showType("org") && (
        <>
          <Chips label="Organization type" options={opts.orgType} value={f.org_type} onChange={(v) => p({ org_type: v })} />
          <Chips label="Region" options={opts.region} value={f.region} onChange={(v) => p({ region: v })} />
          <Chips label="Value chain" options={opts.valueChain} value={f.value_chain} onChange={(v) => p({ value_chain: v })} />
          <Chips label="Sector" options={opts.sector} value={f.sector} onChange={(v) => p({ sector: v })} />
          <Chips label="Relationship potential" options={opts.rel} value={f.relationship} onChange={(v) => p({ relationship: v })} />
        </>
      )}
      {(showType("robot") || showType("org")) && (
        <div className="fgroup">
          <div className="flabel">Open source</div>
          <div className="chips">
            {([[null, "Any"], [true, "Yes"], [false, "No"]] as const).map(([v, l]) => (
              <button key={l} className={"chip" + ((f.open_source ?? null) === v ? " on" : "")} onClick={() => p({ open_source: v })}>{l}</button>
            ))}
          </div>
        </div>
      )}
      {view === "graph" && (
        <div className="fgroup">
          <label className="check"><input type="checkbox" checked={showAllEdges} onChange={(e) => setShowAllEdges(e.target.checked)} /> Show all links (not just prerequisites)</label>
          <label className="check"><input type="checkbox" checked={hideIsolated} onChange={(e) => setHideIsolated(e.target.checked)} /> When filtering, hide robots/orgs not linked to a visible project</label>
        </div>
      )}
      <button className="reset" onClick={() => setFilters(view, view === "graph" ? { types: ["project", "knowledge", "robot"] } : {})}>Reset filters</button>
    </div>
  );
}
