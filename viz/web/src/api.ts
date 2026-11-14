import type { ChatMessage, Filters, GraphData, Group, UiCommand, View } from "./types";

async function j<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, { headers: { "Content-Type": "application/json" }, ...init });
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
  return r.json() as Promise<T>;
}

export const api = {
  data: () => j<GraphData>("/api/data"),
  groups: () => j<Group[]>("/api/groups"),
  createGroup: (body: Partial<Group>) =>
    j<Group>("/api/groups", { method: "POST", body: JSON.stringify({ created_by: "user", ...body }) }),
  patchGroup: (id: string, body: Partial<Group>) =>
    j<Group>(`/api/groups/${id}`, { method: "PATCH", body: JSON.stringify(body) }),
  addToGroup: (id: string, node_ids: string[]) =>
    j<Group>(`/api/groups/${id}/add`, { method: "POST", body: JSON.stringify({ node_ids }) }),
  removeFromGroup: (id: string, node_ids: string[]) =>
    j<Group>(`/api/groups/${id}/remove`, { method: "POST", body: JSON.stringify({ node_ids }) }),
  deleteGroup: (id: string) => j<{ ok: boolean }>(`/api/groups/${id}`, { method: "DELETE" }),
  chatStatus: () => j<{ backend: string; model?: string }>("/api/chat/status"),
};

export function subscribeEvents(onGroups: (g: Group[]) => void, onUi: (c: UiCommand) => void) {
  let es: EventSource | null = null;
  let closed = false;
  const open = () => {
    es = new EventSource("/api/events");
    es.addEventListener("groups", (e) => onGroups(JSON.parse((e as MessageEvent).data)));
    es.addEventListener("ui", (e) => onUi(JSON.parse((e as MessageEvent).data)));
    es.onerror = () => {
      es?.close();
      if (!closed) setTimeout(open, 2000);
    };
  };
  open();
  return () => { closed = true; es?.close(); };
}

export type ChatEvent =
  | { type: "text"; text: string }
  | { type: "tool"; name: string; input: unknown; result_summary?: string }
  | { type: "error"; message: string }
  | { type: "done" };

export async function streamChat(
  messages: ChatMessage[],
  context: { view: View; selected_node_id?: string | null; filters?: Filters; visible_node_ids_count?: number },
  onEvent: (e: ChatEvent) => void,
  signal?: AbortSignal,
) {
  const r = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages: messages.map(({ role, content }) => ({ role, content })), context }),
    signal,
  });
  if (!r.ok || !r.body) {
    onEvent({ type: "error", message: `${r.status} ${await r.text()}` });
    onEvent({ type: "done" });
    return;
  }
  const reader = r.body.getReader();
  const dec = new TextDecoder();
  let buf = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let i;
    while ((i = buf.indexOf("\n\n")) >= 0) {
      const chunk = buf.slice(0, i);
      buf = buf.slice(i + 2);
      for (const line of chunk.split("\n")) {
        if (line.startsWith("data:")) {
          try { onEvent(JSON.parse(line.slice(5).trim())); } catch { /* ignore partial */ }
        }
      }
    }
  }
}
