declare namespace JSX {
  interface IntrinsicElements {
    span: { className?: string; children?: unknown };
    section: { "aria-label"?: string; children?: unknown };
  }
}

interface LabelProps {
  text: string;
  count: number;
}

function Label({ text, count }: LabelProps) {
  if (!text) {
    throw new Error("missing label");
  }

  return <span className="label">{text} ({count})</span>;
}

async function loadLabel() {
  const item: LabelProps = await Promise.resolve({ text: "Hello", count: 3 });
  return <Label text={item.text} count={item.count} />;
}

const preview = <section aria-label="Preview">{loadLabel()}</section>;
