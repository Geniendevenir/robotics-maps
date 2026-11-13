export const BRANCH_COLORS: Record<string, string> = {};
const PALETTE = [
  "#ff6b6b", "#ffa94d", "#ffd43b", "#a9e34b", "#51cf66", "#20c997", "#22b8cf",
  "#339af0", "#5c7cfa", "#845ef7", "#cc5de8", "#f06595", "#e8a87c", "#94d2bd",
];
export function branchColor(branch: string | null | undefined, all: string[]): string {
  if (!branch) return "#adb5bd";
  if (!BRANCH_COLORS[branch]) {
    const i = all.indexOf(branch);
    BRANCH_COLORS[branch] = PALETTE[(i >= 0 ? i : Object.keys(BRANCH_COLORS).length) % PALETTE.length];
  }
  return BRANCH_COLORS[branch];
}
export const TYPE_COLORS = { project: "#f8f9fa", knowledge: "#ffd43b", robot: "#4dabf7", org: "#b197fc" };
export const TYPE_LABELS = { project: "Projects", knowledge: "Knowledge", robot: "Robots & models", org: "Organizations" };
export const ORG_TYPE_COLORS: Record<string, string> = {
  Corporate: "#4dabf7", Startup: "#ff922b", "Research lab": "#51cf66", School: "#ffd43b",
  Association: "#f06595", Investor: "#845ef7", Event: "#22b8cf", Other: "#adb5bd",
};
export const GROUP_COLORS = ["#e4572e", "#29bf12", "#f3a712", "#2e86ab", "#a23b72", "#00b4d8", "#ff70a6", "#8ac926"];
