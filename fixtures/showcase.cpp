#include <stdexcept>
#include <string>
#include <string_view>

namespace preview {
constexpr int max_labels = 3;

class LabelRenderer {
public:
    explicit LabelRenderer(std::string prefix) : prefix_(prefix) {}

    [[nodiscard]] std::string render(std::string_view label, int count) const {
        if (count > max_labels) {
            throw std::out_of_range("too many labels");
        }
        std::string result = prefix_;
        for (int index = 0; index < count; ++index) {
            result += label;
        }
        return result;
    }

private:
    std::string prefix_;
};
} // namespace preview
