import type { ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import Mermaid from "./Mermaid";

type HastNode = { type: string; value?: string; tagName?: string; properties?: Record<string, unknown>; children?: HastNode[] };

const textOf = (n?: HastNode): string => (n ? (n.value ?? "") + (n.children ?? []).map(textOf).join("") : "");

const CALLOUTS: [RegExp, string][] = [
  [/^\s*key idea\b/i, "key"],
  [/^\s*watch out\b/i, "warn"],
  [/^\s*try (this|it)\b/i, "try"],
];

export default function Markdown({ text }: { text: string }) {
  return (
    <div className="md">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ node: _n, ...p }) => <a {...p} target="_blank" rel="noreferrer" />,
          img: ({ node: _n, alt, ...p }) => <img {...p} alt={alt ?? ""} loading="lazy" />,
          pre: ({ node, children }) => {
            const code = (node as HastNode | undefined)?.children?.[0];
            const cls = code?.properties?.className;
            if (Array.isArray(cls) && cls.includes("language-mermaid")) return <Mermaid code={textOf(code).trim()} />;
            return <pre>{children}</pre>;
          },
          blockquote: ({ node, children }: { node?: unknown; children?: ReactNode }) => {
            const kind = CALLOUTS.find(([re]) => re.test(textOf(node as HastNode)))?.[1];
            return <blockquote className={kind ? `callout callout-${kind}` : undefined}>{children}</blockquote>;
          },
        }}
      >
        {text}
      </ReactMarkdown>
    </div>
  );
}
