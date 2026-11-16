export class LabelRenderer {
  readonly prefix = "rose";

  render(label: string): string {
    if (label.length === 0) {
      throw new Error("A label is required");
    }
    return `${this.prefix}: ${label}`;
  }
}
