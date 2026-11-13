import { useEffect, useMemo, useRef, useState } from "react";
import cytoscape, { Core } from "cytoscape";
import { useStore } from "../store";
import { holygraphLayout, R0, RING } from "../layout";
import { nodeMatches, hasConstraints } from "../filters";
import { branchColor, TYPE_COLORS } from "../colors";
import type { MapNode } from "../types";

function wow(n: MapNode) {
  const w = parseFloat(String(n.fields["Wow factor"] ?? ""));
  return isNaN(w) ? 3 : w;
}

export default function GraphView() {
  const ref = useRef<HTMLDivElement>(null);
  const cyRef = useRef<Core | null>(null);
  const { data, index, groups, filters, selectedId, highlight, focusTick, showAllEdges, hideIsolated, multi } = useStore();
  const select = useStore((s) => s.select);
  const setMulti = useStore((s) => s.setMulti);
  const [layoutMode, setLayoutMode] = useState<"rings" | "force">("rings");
  const f = filters.graph;

  const visible = useMemo(() => {
    if (!data || !index) return new Set<string>();
    const base = new Set(data.nodes.filter((n) => nodeMatches(n, f, groups)).map((n) => n.id));
    if (!hideIsolated || !hasConstraints(f) || f.group_id) return base;
    // keep robots/orgs/knowledge only if they connect to a visible project or knowledge node
    const out = new Set<string>();
    for (const id of base) {
      const n = index.byId.get(id)!;
      if (n.type === "project") { out.add(id); continue; }
      const nb = index.adj.get(id) ?? [];
      const constrainedSelf = n.type === "knowledge" ? (f.branches?.length || f.knowledge_level?.length || f.search) : f.search || f.robot_kind?.length || f.open_source != null;
      if (constrainedSelf && n.type === "knowledge") { out.add(id); continue; }
      if (nb.some((e) => base.has(e.id) && index.byId.get(e.id)!.type === "project")) out.add(id);
      else if (n.type !== "knowledge" && constrainedSelf) out.add(id);
    }
    return out;
  }, [data, index, f, groups, hideIsolated]);

  // init
  useEffect(() => {
    if (!data || !index || !ref.current) return;
    const pos = holygraphLayout(data.nodes, index);
    const els: cytoscape.ElementDefinition[] = [];
    for (let l = 1; l <= 5; l++) {
      const r = R0 + (l - 1) * RING;
      els.push({ data: { id: `ring${l}`, label: `Level ${l}`, d: 2 * r }, position: { x: 0, y: 0 }, classes: "ring", selectable: false, grabbable: false });
    }
    for (const b of index.branches) {
      const i = index.branches.indexOf(b);
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / index.branches.length;
      const r = R0 + 4.6 * RING;
      els.push({ data: { id: `blabel-${i}`, label: b.toUpperCase(), color: branchColor(b, index.branches) }, position: { x: r * Math.cos(a), y: r * Math.sin(a) }, classes: "blabel", selectable: false, grabbable: false });
    }
    for (const n of data.nodes) {
      const p = pos.get(n.id) ?? { x: 0, y: 0 };
      const color = n.type === "project" || n.type === "knowledge" ? branchColor(n.branch, index.branches) : TYPE_COLORS[n.type];
      const size = n.type === "project" ? (n.level === 0 ? 46 : 18 + wow(n) * 5) : n.type === "knowledge" ? 34 : 38;
      els.push({
        data: { id: n.id, label: n.name, color, size, img: n.image ?? "", type: n.type },
        position: p,
        classes: [n.type, n.image ? "img" : "", n.level === 0 ? "onboarding" : ""].join(" "),
      });
    }
    for (const [i, e] of data.edges.entries()) {
      if (!index.byId.has(e.source) || !index.byId.has(e.target)) continue;
      els.push({ data: { id: `e${i}`, source: e.source, target: e.target, kind: e.kind }, classes: e.kind === "prerequisite" ? "prereq" : "rel" });
    }
    const cy = cytoscape({
      container: ref.current,
      elements: els,
      layout: { name: "preset" },
      wheelSensitivity: 1.2,
      minZoom: 0.03,
      maxZoom: 3,
      boxSelectionEnabled: true,
      selectionType: "additive",
      textureOnViewport: true,
      hideEdgesOnViewport: true,
      pixelRatio: 1,
      style: [
        { selector: "node", style: {
          "background-color": "data(color)", width: "data(size)", height: "data(size)",
          label: "data(label)", color: "#e9ecef", "font-size": 11, "text-valign": "bottom", "text-margin-y": 4,
          "text-wrap": "ellipsis", "text-max-width": "130px", "min-zoomed-font-size": 9,
          "text-outline-color": "#0d1117", "text-outline-width": 2, "border-width": 0,
        } },
        { selector: "node.knowledge", style: { shape: "round-hexagon", "background-opacity": 0.85, "border-width": 2, "border-color": "#0d1117", "font-weight": "bold" } },
        { selector: "node.robot", style: { shape: "round-rectangle", "background-color": "#1c2a3a", "border-width": 2, "border-color": "#4dabf7" } },
        { selector: "node.org", style: { shape: "ellipse", "background-color": "#241f36", "border-width": 2, "border-color": "#b197fc" } },
        { selector: "node.img", style: { "background-image": "data(img)", "background-fit": "contain", "background-color": "#ffffff", "background-clip": "node", "background-image-containment": "inside", "background-width": "80%", "background-height": "80%" } },
        { selector: "node.onboarding", style: { "border-width": 3, "border-color": "#ffffff", "font-size": 13, "font-weight": "bold" } },
        { selector: "node.ring", style: { width: "data(d)", height: "data(d)", "background-opacity": 0, "border-width": 1, "border-color": "#30363d", "border-style": "dashed", label: "data(label)", "text-valign": "top", "text-margin-y": 18, color: "#6e7681", "font-size": 22, events: "no", "z-index": 0, "min-zoomed-font-size": 0 } },
        { selector: "node.blabel", style: { width: 1, height: 1, "background-opacity": 0, label: "data(label)", color: "data(color)", "font-size": 64, "font-weight": "bold", "text-valign": "center", events: "no", "min-zoomed-font-size": 0, "text-outline-width": 0, "text-max-width": "1200px" } },
        { selector: "edge", style: { width: 1, "line-color": "#3d4450", opacity: 0.5, "curve-style": "haystack" } },
        { selector: "edge.prereq", style: { "curve-style": "straight", "target-arrow-shape": "triangle", "arrow-scale": 0.8, "line-color": "#6e7681", "target-arrow-color": "#6e7681", width: 1.2, opacity: 0.55 } },
        { selector: "edge.rel", style: { display: "none" } },
        { selector: "edge.rel.show", style: { display: "element" } },
        { selector: ".hidden", style: { display: "none" } },
        { selector: ".dim", style: { opacity: 0.12 } },
        { selector: "edge.nb", style: { opacity: 0.95, width: 2, "line-color": "#f8f9fa", "target-arrow-color": "#f8f9fa", "z-index": 9 } },
        { selector: "node.hl", style: { "border-width": 5, "border-color": "#ffd43b", "z-index": 10 } },
        { selector: "node.grp", style: { "border-width": 4, "border-color": "data(gcolor)" } },
        { selector: "node:selected", style: { "border-width": 5, "border-color": "#ff6b6b", "z-index": 11 } },
      ],
    });
    cy.on("tap", "node", (e) => {
      const id = e.target.id();
      if (id.startsWith("ring") || id.startsWith("blabel")) return;
      const oe = e.originalEvent as MouseEvent | undefined;
      if (oe && (oe.shiftKey || oe.metaKey || oe.ctrlKey)) return;
      select(id);
    });
    cy.on("tap", (e) => { if (e.target === cy) { select(null); cy.$(":selected").unselect(); setMulti([]); } });
    const syncMulti = () => setMulti(cy.$("node:selected").map((n) => n.id()));
    cy.on("select unselect", "node", () => { clearTimeout((cy as any)._mt); (cy as any)._mt = setTimeout(syncMulti, 50); });
    cy.fit(cy.nodes(".project, .knowledge"), 20);
    cyRef.current = cy;
    return () => { cy.destroy(); cyRef.current = null; };
  }, [data, index]);

  // visibility + edges + highlight
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy || !index) return;
    const sel = selectedId && visible.has(selectedId) ? selectedId : null;
    const nb = new Set<string>();
    if (sel) { nb.add(sel); for (const e of index.adj.get(sel) ?? []) nb.add(e.id); }
    const hl = new Set(highlight);
    const groupColor = new Map<string, string>();
    if (f.group_id) { const g = groups.find((x) => x.id === f.group_id); g?.node_ids.forEach((id) => groupColor.set(id, g.color)); }
    cy.batch(() => {
      cy.nodes().forEach((n) => {
        const id = n.id();
        if (id.startsWith("ring") || id.startsWith("blabel")) {
          n.toggleClass("hidden", layoutMode === "force");
          return;
        }
        n.toggleClass("hidden", !visible.has(id));
        n.toggleClass("dim", (sel != null && !nb.has(id)) || (hl.size > 0 && !hl.has(id) && !nb.has(id)));
        n.toggleClass("hl", hl.has(id));
        const gc = groupColor.get(id);
        n.toggleClass("grp", !!gc);
        if (gc) n.data("gcolor", gc);
      });
      cy.edges().forEach((e) => {
        const s = e.data("source"), t = e.data("target");
        const vis = visible.has(s) && visible.has(t);
        const touches = sel != null && (s === sel || t === sel);
        e.toggleClass("hidden", !vis);
        e.toggleClass("show", vis && (showAllEdges || touches));
        e.toggleClass("nb", touches);
        e.toggleClass("dim", (sel != null && !touches) || (hl.size > 0 && !(hl.has(s) && hl.has(t))));
      });
    });
  }, [visible, selectedId, highlight, showAllEdges, index, layoutMode, f.group_id, groups]);

  // sync cytoscape selection with store selection
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;
    if (multi.length === 0) cy.$("node:selected").unselect();
  }, [multi]);

  // focus
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy || !selectedId || focusTick === 0) return;
    const n = cy.getElementById(selectedId);
    if (n.nonempty()) cy.animate({ center: { eles: n }, zoom: Math.max(cy.zoom(), 1.1) }, { duration: 500 });
  }, [focusTick]);

  // fit to highlight
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy || highlight.length === 0) return;
    let els = cy.collection();
    for (const id of highlight) els = els.union(cy.getElementById(id));
    if (els.nonempty()) cy.animate({ fit: { eles: els, padding: 80 } }, { duration: 500 });
  }, [highlight]);

  const runLayout = (mode: "rings" | "force") => {
    const cy = cyRef.current;
    if (!cy || !data || !index) return;
    setLayoutMode(mode);
    if (mode === "rings") {
      const pos = holygraphLayout(data.nodes, index);
      cy.nodes().forEach((n) => { const p = pos.get(n.id()); if (p) n.position(p); });
      cy.fit(cy.nodes(":visible"), 30);
    } else {
      const eles = cy.elements(":visible").filter((e) => !e.hasClass("ring") && !e.hasClass("blabel"));
      eles.layout({ name: "cose", animate: false, nodeRepulsion: () => 9000, idealEdgeLength: () => 80, numIter: 1500, fit: true, padding: 30 } as any).run();
    }
  };

  return (
    <div className="graph-wrap">
      <div ref={ref} className="cy" />
      <div className="graph-tools">
        <button className={layoutMode === "rings" ? "on" : ""} onClick={() => runLayout("rings")} title="Branch = sector, Level = ring">Holygraph rings</button>
        <button className={layoutMode === "force" ? "on" : ""} onClick={() => runLayout("force")} title="Force layout of visible nodes">Force layout</button>
        <button onClick={() => cyRef.current?.fit(cyRef.current.nodes(":visible"), 30)}>Fit</button>
        <span className="muted">{visible.size} nodes · shift-drag to multi-select</span>
      </div>
    </div>
  );
}
