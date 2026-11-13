import { useEffect, useMemo, useRef } from "react";
import { MapContainer, TileLayer, useMap } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster";
import "leaflet.markercluster/dist/MarkerCluster.css";
import { useStore } from "../store";
import { nodeMatches } from "../filters";
import { ORG_TYPE_COLORS } from "../colors";
import type { MapNode } from "../types";

function esc(s: string) {
  return s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));
}

function icon(n: MapNode, opts: { selected: boolean; hl: boolean; gcolor?: string }) {
  const color = ORG_TYPE_COLORS[String(n.fields["Type"] ?? "Other")] ?? "#adb5bd";
  const inner = n.image
    ? `<img src="${n.image}" alt="" loading="lazy" onerror="this.remove()"/>`
    : `<span>${esc(n.name.slice(0, 2).toUpperCase())}</span>`;
  const cls = ["mk", opts.selected ? "sel" : "", opts.hl ? "hl" : "", n.geo?.approx ? "approx" : ""].join(" ");
  const ring = opts.gcolor ? `box-shadow:0 0 0 4px ${opts.gcolor};` : "";
  return L.divIcon({
    className: "mk-wrap",
    html: `<div class="${cls}" style="border-color:${color};${ring}">${inner}</div><div class="mk-label">${esc(n.name)}</div>`,
    iconSize: [40, 40],
    iconAnchor: [20, 20],
  });
}

function Markers() {
  const map = useMap();
  const { data, groups, filters, selectedId, highlight, focusTick } = useStore();
  const select = useStore((s) => s.select);
  const clusterRef = useRef<L.MarkerClusterGroup | null>(null);
  const markers = useRef(new Map<string, L.Marker>());
  const f = filters.map;

  const orgs = useMemo(
    () => (data?.nodes ?? []).filter((n) => n.type === "org" && n.geo && nodeMatches(n, f, groups, false)),
    [data, f, groups],
  );

  useEffect(() => {
    const hl = new Set(highlight);
    const g = f.group_id ? groups.find((x) => x.id === f.group_id) : undefined;
    const cluster = L.markerClusterGroup({
      maxClusterRadius: 45, showCoverageOnHover: false, spiderfyOnMaxZoom: true, chunkedLoading: true,
      iconCreateFunction: (c) => {
        const ms = c.getAllChildMarkers();
        const imgs = ms.map((m) => (m.options as any).img).filter(Boolean).slice(0, 3);
        return L.divIcon({
          className: "cl-wrap",
          html: `<div class="cl"><div class="cl-imgs">${imgs.map((s: string) => `<img src="${s}" onerror="this.remove()"/>`).join("")}</div><b>${ms.length}</b></div>`,
          iconSize: [56, 56], iconAnchor: [28, 28],
        });
      },
    });
    markers.current.clear();
    for (const n of orgs) {
      const m = L.marker([n.geo!.lat, n.geo!.lon], {
        icon: icon(n, { selected: n.id === selectedId, hl: hl.has(n.id), gcolor: g?.node_ids.includes(n.id) ? g.color : undefined }),
        title: n.name,
        img: n.image,
      } as any);
      m.on("click", () => select(n.id));
      cluster.addLayer(m);
      markers.current.set(n.id, m);
    }
    map.addLayer(cluster);
    clusterRef.current = cluster;
    return () => { map.removeLayer(cluster); };
  }, [orgs, selectedId, highlight, map, f.group_id, groups]);

  useEffect(() => {
    if (!selectedId || focusTick === 0) return;
    const m = markers.current.get(selectedId);
    if (m && clusterRef.current) {
      map.flyTo(m.getLatLng(), Math.max(map.getZoom(), 9), { duration: 0.8 });
      setTimeout(() => clusterRef.current?.zoomToShowLayer(m, () => {}), 900);
    }
  }, [focusTick]);

  useEffect(() => {
    if (highlight.length === 0) return;
    const pts = highlight.map((id) => markers.current.get(id)?.getLatLng()).filter(Boolean) as L.LatLng[];
    if (pts.length) map.flyToBounds(L.latLngBounds(pts).pad(0.3), { duration: 0.8, maxZoom: 10 });
  }, [highlight]);

  return (
    <div className="map-count">
      {orgs.length} organizations{orgs.some((o) => o.geo?.approx) ? " · dashed = approximate location" : ""}
    </div>
  );
}

export default function MapView() {
  return (
    <div className="map-wrap">
      <MapContainer center={[46.5, 8]} zoom={4} minZoom={2} worldCopyJump style={{ height: "100%", width: "100%" }}>
        <TileLayer
          attribution="Tiles &copy; Esri &mdash; Esri, HERE, Garmin, &copy; OpenStreetMap contributors"
          url="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}"
          maxZoom={16}
        />
        <Markers />
      </MapContainer>
    </div>
  );
}
