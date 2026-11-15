import { useEffect, useId, useState } from "react";

let ready: Promise<typeof import("mermaid").default> | null = null;
function loadMermaid() {
  ready ??= import("mermaid").then(({ default: m }) => {
    m.initialize({
      startOnLoad: false,
      securityLevel: "strict",
      theme: "base",
      themeVariables: {
        darkMode: true,
        fontFamily: "inherit",
        fontSize: "15px",
        background: "#0d1117",
        primaryColor: "#1f2630",
        primaryTextColor: "#e6edf3",
        primaryBorderColor: "#ffd43b",
        lineColor: "#74c0fc",
        edgeLabelBackground: "#161b22",
      },
      flowchart: { padding: 14, nodeSpacing: 40, rankSpacing: 46 },
    });
    return m;
  });
  return ready;
}

export default function Mermaid({ code }: { code: string }) {
  const id = "mmd" + useId().replace(/[^a-zA-Z0-9]/g, "");
  const [svg, setSvg] = useState<string | null>(null);
  const [failed, setFailed] = useState(false);
  useEffect(() => {
    let live = true;
    loadMermaid()
      .then((m) => m.render(id, code))
      .then((r) => live && setSvg(r.svg))
      .catch(() => live && setFailed(true));
    return () => {
      live = false;
    };
  }, [id, code]);
  if (failed) return <pre>{code}</pre>;
  return <div className="diagram" dangerouslySetInnerHTML={{ __html: svg ?? "" }} />;
}
