import type { MapNode } from "./types";
import type { Index } from "./store";

// Holygraph layout: Branch = angular sector, Level = ring (onboarding at the centre),
// knowledge just outside the project rings, robots/models and orgs in outer bands
// at the circular mean angle of what they connect to.
export const R0 = 260;
export const RING = 330;

export function holygraphLayout(nodes: MapNode[], index: Index): Map<string, { x: number; y: number }> {
  const pos = new Map<string, { x: number; y: number }>();
  const branches = index.branches;
  const nB = Math.max(branches.length, 1);
  const sector = (2 * Math.PI) / nB;
  const angOfBranch = (b: string | null) => {
    const i = b ? branches.indexOf(b) : -1;
    return i < 0 ? null : -Math.PI / 2 + i * sector;
  };
  const angle = new Map<string, number>();
  const place = (id: string, r: number, a: number) => {
    pos.set(id, { x: r * Math.cos(a), y: r * Math.sin(a) });
    angle.set(id, a);
  };

  // onboarding: inner circle
  const onboarding = nodes.filter((n) => n.type === "project" && n.level === 0);
  onboarding.forEach((n, i) => place(n.id, 120, -Math.PI / 2 + (i / Math.max(onboarding.length, 1)) * 2 * Math.PI));

  // projects by branch + level bucket
  const buckets = new Map<string, MapNode[]>();
  for (const n of nodes) {
    if (n.type !== "project" || n.level === 0) continue;
    const lv = Math.round(((n.level as number) ?? 1) * 3) / 3;
    const k = `${n.branch}|${lv.toFixed(2)}`;
    if (!buckets.has(k)) buckets.set(k, []);
    buckets.get(k)!.push(n);
  }
  let maxProjectR = R0;
  for (const [k, list] of buckets) {
    const [b, lvS] = k.split("|");
    const lv = parseFloat(lvS);
    const base = angOfBranch(b) ?? 0;
    const rBase = R0 + (lv - 1) * RING;
    list.sort((a, b) => a.name.localeCompare(b.name));
    const spacing = 46;
    let placed = 0, row = 0;
    while (placed < list.length) {
      const r = rBase + row * 44;
      const cap = Math.max(1, Math.floor((sector * 0.86 * r) / spacing));
      const take = list.slice(placed, placed + cap);
      take.forEach((n, i) => {
        const t = take.length === 1 ? 0.5 : i / (take.length - 1);
        const jitter = row % 2 ? 0.5 / cap : 0;
        place(n.id, r, base - sector * 0.43 + sector * 0.86 * Math.min(1, t + jitter * (take.length > 1 ? 1 : 0)));
      });
      placed += take.length;
      row++;
      maxProjectR = Math.max(maxProjectR, r);
    }
  }

  // knowledge band
  const kR = maxProjectR + 260;
  const kn = nodes.filter((n) => n.type === "knowledge");
  const kByBranch = new Map<string, MapNode[]>();
  for (const n of kn) {
    const k = n.branch ?? "?";
    if (!kByBranch.has(k)) kByBranch.set(k, []);
    kByBranch.get(k)!.push(n);
  }
  const lvlOrder = { Fundamental: 0, Applied: 1, Frontier: 2 } as Record<string, number>;
  let maxKR = kR;
  for (const [b, list] of kByBranch) {
    const base = angOfBranch(b) ?? 0;
    list.sort((a, c) => (lvlOrder[String(a.level)] ?? 1) - (lvlOrder[String(c.level)] ?? 1) || a.name.localeCompare(c.name));
    const perRow = Math.max(1, Math.floor((sector * 0.86 * kR) / 70));
    list.forEach((n, i) => {
      const row = Math.floor(i / perRow);
      const inRow = Math.min(perRow, list.length - row * perRow);
      const t = inRow === 1 ? 0.5 : (i % perRow) / (inRow - 1);
      const r = kR + row * 70;
      maxKR = Math.max(maxKR, r);
      place(n.id, r, base - sector * 0.43 + sector * 0.86 * t);
    });
  }

  // outer bands: circular mean of neighbour angles, then de-overlap on sub-rings
  const outer = (type: "robot" | "org", rStart: number, gap: number) => {
    const items: { id: string; a: number }[] = [];
    for (const n of nodes) {
      if (n.type !== type) continue;
      let sx = 0, sy = 0, c = 0;
      for (const e of index.adj.get(n.id) ?? []) {
        const a = angle.get(e.id);
        if (a == null) continue;
        sx += Math.cos(a); sy += Math.sin(a); c++;
      }
      const h = [...n.id].reduce((s, ch) => (s * 31 + ch.charCodeAt(0)) >>> 0, 7);
      const a = c ? Math.atan2(sy, sx) : (h % 3600) / 3600 * 2 * Math.PI;
      items.push({ id: n.id, a });
    }
    items.sort((p, q) => p.a - q.a);
    const lastOnRing: number[] = [];
    let maxR = rStart;
    for (const it of items) {
      let ring = 0;
      for (;;) {
        const r = rStart + ring * gap;
        const minDa = (gap * 0.95) / r;
        if (lastOnRing[ring] == null || it.a - lastOnRing[ring] >= minDa) {
          lastOnRing[ring] = it.a;
          place(it.id, r, it.a);
          maxR = Math.max(maxR, r);
          break;
        }
        ring++;
      }
    }
    return maxR;
  };
  const rMax = outer("robot", maxKR + 240, 64);
  outer("org", rMax + 260, 64);
  return pos;
}
