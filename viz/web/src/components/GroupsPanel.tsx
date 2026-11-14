import { useState } from "react";
import { useStore } from "../store";
import { api } from "../api";
import { GROUP_COLORS } from "../colors";
import { NodeChip } from "./SidePanel";

export default function GroupsPanel() {
  const { groups, view, filters, multi } = useStore();
  const patch = useStore((s) => s.patchFilters);
  const setHighlight = useStore((s) => s.setHighlight);
  const [name, setName] = useState("");
  const [open, setOpen] = useState<string | null>(null);
  const [editing, setEditing] = useState<string | null>(null);
  const create = async () => {
    if (!name.trim()) return;
    await api.createGroup({ name: name.trim(), node_ids: multi, color: GROUP_COLORS[groups.length % GROUP_COLORS.length] });
    setName("");
  };
  return (
    <div className="groups">
      <div className="gnew">
        <input placeholder={multi.length ? `New group with ${multi.length} selected nodes` : "New group name"} value={name}
          onChange={(e) => setName(e.target.value)} onKeyDown={(e) => e.key === "Enter" && create()} />
        <button onClick={create}>Create</button>
      </div>
      {groups.length === 0 && <div className="muted">No groups yet. Create one here, from a node's panel, or ask the guide to build one.</div>}
      {groups.map((g) => {
        const active = filters[view].group_id === g.id;
        return (
          <div key={g.id} className={"gcard" + (active ? " active" : "")} style={{ borderLeftColor: g.color }}>
            <div className="grow">
              {editing === g.id ? (
                <input autoFocus defaultValue={g.name} onBlur={async (e) => { await api.patchGroup(g.id, { name: e.target.value }); setEditing(null); }}
                  onKeyDown={(e) => e.key === "Enter" && (e.target as HTMLInputElement).blur()} />
              ) : (
                <b onDoubleClick={() => setEditing(g.id)} title="double-click to rename">{g.name}</b>
              )}
              <span className="muted small">{g.node_ids.length} nodes · {g.created_by === "agent" ? "by guide" : "by you"}</span>
            </div>
            {g.description && <div className="muted small">{g.description}</div>}
            <div className="gactions">
              <button className={active ? "on" : ""} onClick={() => patch(view, { group_id: active ? null : g.id })}>{active ? "Showing" : "Show only"}</button>
              <button onClick={() => setHighlight(g.node_ids)}>Highlight</button>
              <button onClick={() => setOpen(open === g.id ? null : g.id)}>{open === g.id ? "Hide" : "Members"}</button>
              {multi.length > 0 && <button onClick={() => api.addToGroup(g.id, multi)}>+ {multi.length} selected</button>}
              <button className="danger" onClick={() => { if (confirm(`Delete group "${g.name}"?`)) api.deleteGroup(g.id); }}>Delete</button>
            </div>
            {open === g.id && (
              <div className="chiplist">
                {g.node_ids.map((id) => (
                  <span key={id} className="member"><NodeChip id={id} /><button className="link" onClick={() => api.removeFromGroup(g.id, [id])}>×</button></span>
                ))}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
