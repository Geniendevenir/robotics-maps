export type NodeType = "project" | "knowledge" | "robot" | "org";
export type View = "graph" | "map";

export interface Geo { lat: number; lon: number; place: string; approx: boolean }

export interface MapNode {
  id: string;
  type: NodeType;
  name: string;
  branch: string | null;
  level: number | string | null;
  image: string | null;
  notion_url: string | null;
  geo?: Geo | null;
  fields: Record<string, unknown>;
}

export type EdgeKind =
  | "prerequisite" | "project-knowledge" | "project-robot" | "project-org"
  | "robot-knowledge" | "robot-builder" | "robot-user";

export interface MapEdge { source: string; target: string; kind: EdgeKind }

export interface GraphData { generated_at: string; nodes: MapNode[]; edges: MapEdge[] }

export interface Group {
  id: string; name: string; description: string; color: string;
  node_ids: string[]; created_by: "user" | "agent"; created_at: string; updated_at: string;
}

export interface Filters {
  search?: string;
  types?: NodeType[];
  branches?: string[];
  level_min?: number | null;
  level_max?: number | null;
  project_kind?: string[];
  knowledge_level?: string[];
  robot_kind?: string[];
  hardware_cost?: string[];
  org_type?: string[];
  region?: string[];
  value_chain?: string[];
  sector?: string[];
  relationship?: string[];
  open_source?: boolean | null;
  group_id?: string | null;
}

export type UiCommand =
  | { action: "focus"; node_id: string }
  | { action: "highlight"; node_ids: string[] }
  | { action: "set_filters"; view: View; filters: Filters }
  | { action: "show_group"; group_id: string }
  | { action: "switch_view"; view: View };

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  tools?: { name: string; input: unknown; result_summary?: string }[];
}
