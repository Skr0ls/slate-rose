package preview;

import java.util.List;

public class PrimitiveTypes {
    private int count = 2;
    private boolean enabled = true;
    private float scale = 1.5f;
    private String label = "samples";
    private Integer boxedCount = 3;
    private Boolean boxedEnabled = Boolean.TRUE;
    private List<Integer> values = List.of(boxedCount);

    public int measure(int input, boolean active, float factor) {
        int total = input + count;
        boolean ready = active && enabled;
        float adjusted = total * factor * scale;
        int[] samples = {total, (int) adjusted};
        var inferred = samples.length;
        int record = inferred;
        if (ready) {
            return samples[0] + record + values.size();
        }
        throw new IllegalStateException(label);
    }

    public boolean isEnabled(boolean fallback) {
        return boxedEnabled != null ? boxedEnabled : fallback;
    }

    public float scaled(float value) {
        return value * scale;
    }

    public void reset() {
        count = 0;
    }
}
