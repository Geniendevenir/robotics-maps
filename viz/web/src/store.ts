import { create } from "zustand";
import type { ChatMessage, Filters, GraphData, Group, MapEdge, MapNode, View } from "./types";

export interface Index {
  byId: Map<string, MapNode>;
  adj: Map<string, { id: string; kind: MapEdge["kind"]; dir: "out" | "in" }[]>;
  branches: string[];
}

export function buildIndex(d: GraphData): Index {
  const byId = new Map(d.nodes.map((n) => [n.id, n]));
  const adj: Index["adj"] = new Map();
  const push = (a: string, v: { id: string; kind: MapEdge["kind"]; dir: "out" | "in" }) => {
    if (!adj.has(a)) adj.set(a, []);
    adj.get(a)!.push(v);
  };
  for (const e of d.edges) {
    if (!byId.has(e.source) || !byId.has(e.target)) continue;
    push(e.source, { id: e.target, kind: e.kind, dir: "out" });
    push(e.target, { id: e.source, kind: e.kind, dir: "in" });
  }
  const bc = new Map<string, number>();
  for (const n of d.nodes) if (n.branch) bc.set(n.branch, (bc.get(n.branch) ?? 0) + 1);
  const branches = [...bc.keys()].sort();
  return { byId, adj, branches };
}

export type RightTab = "details" | "groups" | "chat";

interface State {
  data: GraphData | null;
  index: Index | null;
  groups: Group[];
  view: View;
  filters: Record<View, Filters>;
  selectedId: string | null;
  multi: string[];
  highlight: string[];
  rightTab: RightTab;
  rightOpen: boolean;
  focusTick: number;
  chat: ChatMessage[];
  showAllEdges: boolean;
  hideIsolated: boolean;
  learn: boolean;
  chapterId: string;
  setLearn: (b: boolean) => void;
  setChapter: (id: string) => void;
  setData: (d: GraphData) => void;
  setGroups: (g: Group[]) => void;
  setView: (v: View) => void;
  setFilters: (v: View, f: Filters) => void;
  patchFilters: (v: View, f: Partial<Filters>) => void;
  select: (id: string | null, opts?: { focus?: boolean }) => void;
  setMulti: (ids: string[]) => void;
  setHighlight: (ids: string[]) => void;
  setRightTab: (t: RightTab) => void;
  setRightOpen: (o: boolean) => void;
  setChat: (fn: (c: ChatMessage[]) => ChatMessage[]) => void;
  setShowAllEdges: (b: boolean) => void;
  setHideIsolated: (b: boolean) => void;
}

const initialFilters: Record<View, Filters> = {
  graph: { types: ["project", "knowledge", "robot"] },
  map: {},
};

export const useStore = create<State>((set, get) => ({
  data: null,
  index: null,
  groups: [],
  view: "graph",
  filters: initialFilters,
  selectedId: null,
  multi: [],
  highlight: [],
  rightTab: "chat",
  rightOpen: true,
  focusTick: 0,
  chat: [],
  showAllEdges: false,
  hideIsolated: true,
  learn: false,
  chapterId: "intro",
  setLearn: (learn) => set({ learn, multi: [] }),
  setChapter: (chapterId) => set({ chapterId, learn: true }),
  setData: (d) => set({ data: d, index: buildIndex(d) }),
  setGroups: (groups) => set((state) => {
    const groupIds = new Set(groups.map((group) => group.id));
    let filters = state.filters;
    for (const view of ["graph", "map"] as const) {
      const groupId = filters[view].group_id;
      if (groupId && !groupIds.has(groupId)) {
        if (filters === state.filters) filters = { ...state.filters };
        const nextFilter = { ...filters[view] };
        delete nextFilter.group_id;
        filters = { ...filters, [view]: nextFilter };
      }
    }
    return filters === state.filters ? { groups } : { groups, filters };
  }),
  setView: (view) => set((state) => state.view === view && !state.learn ? state : { view, learn: false, multi: [] }),
  setFilters: (v, f) => set({ filters: { ...get().filters, [v]: f } }),
  patchFilters: (v, f) => set({ filters: { ...get().filters, [v]: { ...get().filters[v], ...f } } }),
  select: (id, opts) => {
    const s: Partial<State> = { selectedId: id };
    if (id) { s.rightTab = "details"; s.rightOpen = true; }
    if (id && opts?.focus) {
      const n = get().index?.byId.get(id);
      if (n && get().learn) {
        // Stay in the Learn view; the details panel shows the node.
      } else if (n) {
        s.focusTick = get().focusTick + 1;
        if (n.type === "org" && get().view === "graph" && !(get().filters.graph.types ?? []).includes("org") && n.geo) s.view = "map";
        else if (n.type !== "org" && get().view === "map") s.view = "graph";
        const v = (s.view ?? get().view) as View;
        if (v === "graph") {
          const types = get().filters.graph.types ?? [];
          if (types.length && !types.includes(n.type)) {
            s.filters = { ...get().filters, graph: { ...get().filters.graph, types: [...types, n.type] } };
          }
        }
      }
    }
    if (opts?.focus || (s.view ?? get().view) === "map") s.multi = [];
    set(s);
  },
  setMulti: (multi) => set({ multi }),
  setHighlight: (highlight) => set({ highlight }),
  setRightTab: (rightTab) => set({ rightTab, rightOpen: true }),
  setRightOpen: (rightOpen) => set({ rightOpen }),
  setChat: (fn) => set({ chat: fn(get().chat) }),
  setShowAllEdges: (showAllEdges) => set({ showAllEdges }),
  setHideIsolated: (hideIsolated) => set({ hideIsolated }),
}));
