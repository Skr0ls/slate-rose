"""Small syntax sample for reviewing the Slate Rose theme."""

from dataclasses import dataclass

MAX_LABELS: int = 3


@dataclass
class LabelRenderer:
    prefix: str

    def render(self, label: str, count: int) -> str:
        if count > MAX_LABELS:
            raise ValueError("too many labels")
        result: str = self.prefix
        for _ in range(count):
            result += label
        return result
