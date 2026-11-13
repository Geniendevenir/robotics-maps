import type { Filters, Group, MapNode } from "./types";

const str = (v: unknown) => (v == null ? "" : Array.isArray(v) ? v.join(" ") : String(v));
const arr = (v: unknown): string[] => (Array.isArray(v) ? v.map(String) : v == null || v === "" ? [] : [String(v)]);
const any = (have: string[], want?: string[]) => !want || want.length === 0 || have.some((h) => want.includes(h));
const isOpen = (v: unknown) => v === true || v === "__YES__" || v === "Yes" || v === "true";

const SEARCH_FIELDS = [
  "What it is", "Description", "Deliverable", "What they build", "Why it matters", "Key specs",
  "Key players", "City", "Builder (if not in map)",
];

export function searchText(n: MapNode) {
  return (n.name + " " + SEARCH_FIELDS.map((f) => str(n.fields[f])).join(" ")).toLowerCase();
}

export function hasConstraints(f: Filters) {
  return Object.entries(f).some(([k, v]) =>
    k !== "types" && v != null && v !== "" && !(Array.isArray(v) && v.length === 0));
}

export function nodeMatches(n: MapNode, f: Filters, groups: Group[], useTypes = true): boolean {
  if (useTypes && f.types && f.types.length && !f.types.includes(n.type)) return false;
  if (f.group_id) {
    const g = groups.find((x) => x.id === f.group_id);
    if (!g || !g.node_ids.includes(n.id)) return false;
  }
  if (f.search && f.search.trim()) {
    const q = f.search.trim().toLowerCase();
    if (!searchText(n).includes(q)) return false;
  }
  const F = n.fields;
  if (n.type === "project" || n.type === "knowledge") {
    const br = [n.branch ?? "", ...arr(F["Secondary branches"])];
    if (!any(br, f.branches)) return false;
  }
  if (n.type === "project") {
    const lvl = typeof n.level === "number" ? n.level : 0;
    if (f.level_min != null && lvl < f.level_min) return false;
    if (f.level_max != null && lvl > f.level_max) return false;
    if (!any(arr(F["Kind"]), f.project_kind)) return false;
    if (!any(arr(F["Hardware cost"]), f.hardware_cost)) return false;
  }
  if (n.type === "knowledge" && !any(arr(n.level), f.knowledge_level)) return false;
  if (n.type === "robot" && !any(arr(F["Kind"]), f.robot_kind)) return false;
  if (n.type === "org") {
    if (!any(arr(F["Type"]), f.org_type)) return false;
    if (!any(arr(F["Region"]), f.region)) return false;
    if (!any(arr(F["Value chain"]), f.value_chain)) return false;
    if (!any(arr(F["Sector"]), f.sector)) return false;
    if (!any(arr(F["Relationship potential"]), f.relationship)) return false;
  }
  if ((n.type === "robot" || n.type === "org") && f.open_source != null) {
    if (isOpen(F["Open source"]) !== f.open_source) return false;
  }
  return true;
}

export function optionValues(nodes: MapNode[], type: MapNode["type"], field: string): string[] {
  const s = new Set<string>();
  for (const n of nodes) if (n.type === type) for (const v of arr(field === "__level" ? n.level : n.fields[field])) if (v) s.add(v);
  return [...s].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
}

export { arr, str, isOpen };
