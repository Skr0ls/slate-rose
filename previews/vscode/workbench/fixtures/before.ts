export class LabelRenderer {
  readonly prefix = "old";

  render(label: string): string {
    const legacy = "remove this label";
    return `${this.prefix}: ${label} ${legacy}`;
  }
}
