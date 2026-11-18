using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace SlateRoseReview;

public class BuiltinTypes
{
    private int count;
    private string label = "ready";
    private float ratio;
    private bool enabled;

    public int Count(int value) => count + value;
    public string Label(string value) => label + value;
    public float Ratio(float value) => ratio + value;
    public bool Enabled(bool value) => enabled && value;

    public Task<String> Review(int input, string text, float amount, bool flag)
    {
        int localCount = (int)amount;
        string localText = text;
        float localRatio = input;
        bool localFlag = flag;
        int? optional = localCount;
        List<string> labels = new() { localText };
        var inferred = labels.Count;
        int @event = inferred;
        System.String qualified = labels[0];

        if (localFlag && optional.HasValue)
        {
            return Task.FromResult(qualified + @event + localRatio);
        }

        return Task.FromResult(String.Empty);
    }
}
