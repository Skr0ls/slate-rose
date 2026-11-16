<?php

namespace Preview;

/** Renders a bounded set of labels for visual review. */
class LabelRenderer
{
    private const MaxLabels = 3;
    private string $prefix;

    public function __construct(string $prefix)
    {
        $this->prefix = $prefix;
    }

    public function render(string $label, int $count): string
    {
        if ($count > self::MaxLabels) {
            throw new \InvalidArgumentException("too many labels");
        }

        $result = "";
        for ($index = 0; $index < $count; $index++) {
            $result .= "{$this->prefix}: {$label} {$index}\n";
        }

        return $result;
    }
}
