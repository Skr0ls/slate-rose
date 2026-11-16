# Renders a bounded set of labels for visual review.
module Preview
  class LabelRenderer
    MAX_LABELS = 3

    def initialize(prefix)
      @prefix = prefix
    end

    def render(label, count)
      if count > MAX_LABELS
        raise ArgumentError, "too many labels"
      end

      result = ""
      count.times do |index|
        result << "#{@prefix}: #{label} #{index}\n"
      end

      return result
    end
  end
end
