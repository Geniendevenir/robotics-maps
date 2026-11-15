import { useEffect, useState } from "react";
import { useStore } from "./store";
import { api, subscribeEvents } from "./api";
import GraphView from "./components/GraphView";
import MapView from "./components/MapView";
import FilterPanel from "./components/FilterPanel";
import SidePanel from "./components/SidePanel";
import GroupsPanel from "./components/GroupsPanel";
import ChatPanel from "./components/ChatPanel";
import LearnView from "./components/LearnView";
import type { UiCommand } from "./types";

function handleUi(c: UiCommand) {
  const s = useStore.getState();
  switch (c.action) {
    case "focus": s.select(c.node_id, { focus: true }); break;
    case "highlight": s.setHighlight(c.node_ids); break;
    case "set_filters": s.setFilters(c.view, c.filters); s.setView(c.view); break;
    case "show_group": s.patchFilters(s.view, { group_id: c.group_id }); break;
    case "switch_view": s.setView(c.view); break;
  }
}

export default function App() {
  const { data, view, rightTab, rightOpen, groups, highlight, learn } = useStore();
  const st = useStore.getState();
  const [err, setErr] = useState<string | null>(null);
  const [leftOpen, setLeftOpen] = useState(true);
  useEffect(() => {
    api.data().then(st.setData).catch((e) => setErr(String(e)));
    api.groups().then(st.setGroups).catch(() => {});
    return subscribeEvents(st.setGroups, handleUi);
  }, []);
  if (err) return <div className="loading">Could not load data: {err}<br />Is the server running on :8765?</div>;
  if (!data) return <div className="loading">Loading maps…</div>;
  return (
    <div className={"app" + (leftOpen && !learn ? "" : " no-left") + (rightOpen ? "" : " no-right") + (learn ? " learning" : "")}>
      <header>
        <div className="brand">42AI Robotics Maps</div>
        <nav>
          <button className={learn ? "on" : ""} onClick={() => st.setLearn(true)}>Learn</button>
          <button className={!learn && view === "graph" ? "on" : ""} onClick={() => st.setView("graph")}>Holygraph whiteboard</button>
          <button className={!learn && view === "map" ? "on" : ""} onClick={() => st.setView("map")}>World map</button>
        </nav>
        <div className="hright">
          {highlight.length > 0 && <button onClick={() => st.setHighlight([])}>Clear highlight ({highlight.length})</button>}
          {!learn && <button onClick={() => setLeftOpen(!leftOpen)}>{leftOpen ? "Hide filters" : "Filters"}</button>}
          <button onClick={() => st.setRightOpen(!rightOpen)}>{rightOpen ? "Hide panel" : "Panel"}</button>
        </div>
      </header>
      {leftOpen && !learn && <aside className="left"><FilterPanel /></aside>}
      <main>{learn ? <LearnView /> : view === "graph" ? <GraphView /> : <MapView />}</main>
      {rightOpen && (
        <aside className="right">
          <div className="tabs">
            <button className={rightTab === "details" ? "on" : ""} onClick={() => st.setRightTab("details")}>Details</button>
            <button className={rightTab === "groups" ? "on" : ""} onClick={() => st.setRightTab("groups")}>Groups ({groups.length})</button>
            <button className={rightTab === "chat" ? "on" : ""} onClick={() => st.setRightTab("chat")}>Guide</button>
          </div>
          <div className="tabbody">
            <div style={{ display: rightTab === "details" ? "block" : "none" }}><SidePanel /></div>
            <div style={{ display: rightTab === "groups" ? "block" : "none" }}><GroupsPanel /></div>
            <div style={{ display: rightTab === "chat" ? "flex" : "none" }} className="chat-host"><ChatPanel /></div>
          </div>
        </aside>
      )}
    </div>
  );
}
