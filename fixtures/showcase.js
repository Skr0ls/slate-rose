class LabelRenderer {
  constructor(prefix) {
    this.prefix = prefix;
  }

  async render(label) {
    if (!label) {
      throw new Error("missing label");
    }

    const result = await Promise.resolve(label.trim());
    return `${this.prefix}: ${result}`;
  }
}

const renderer = new LabelRenderer("Item");
const count = 3;
renderer.render(`Label ${count}`);
