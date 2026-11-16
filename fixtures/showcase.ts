const MAX_LABELS: number = 3;

function describe<T extends new (...args: never[]) => object>(value: T): T {
  return value;
}

@describe
class LabelRenderer {
  constructor(private readonly prefix: string) {}

  get Prefix(): string {
    return this.prefix;
  }

  async render(label: string, count: number): Promise<string> {
    await Promise.resolve();
    if (count > MAX_LABELS) {
      throw new RangeError("too many labels");
    }
    let result: string = this.prefix;
    for (let index = 0; index < count; index++) {
      result += label;
    }
    return result;
  }
}

export { LabelRenderer };
