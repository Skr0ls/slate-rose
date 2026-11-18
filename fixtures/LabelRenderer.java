package preview;

public class LabelRenderer {
    private static final int MAX_LABELS = 3;
    private final String prefix;

    public LabelRenderer(String prefix) {
        this.prefix = prefix;
    }

    public String getPrefix() {
        return prefix;
    }

    public String render(String label, int count) {
        if (count > MAX_LABELS) {
            throw new IllegalArgumentException("count exceeds the maximum");
        }
        String result = prefix;
        for (int index = 0; index < count; index++) {
            result += label;
        }
        return result;
    }
}
