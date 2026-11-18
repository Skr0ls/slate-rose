function Label({ text, count }) {
  if (!text) {
    throw new Error("missing label");
  }

  return <span className="label">{text} ({count})</span>;
}

async function loadLabel() {
  const item = await Promise.resolve({ text: "Hello", count: 3 });
  return <Label text={item.text} count={item.count} />;
}

const preview = <section aria-label="Preview">{loadLabel()}</section>;
