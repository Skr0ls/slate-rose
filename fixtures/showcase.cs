using System;
using System.ComponentModel;
using System.Threading.Tasks;

namespace Preview;

[Description("Renders a short label")]
public class LabelRenderer
{
    private const int MaxLabels = 3;
    private readonly string prefix;

    public string Prefix => prefix;

    public LabelRenderer(string prefix)
    {
        this.prefix = prefix;
    }

    public async Task<string> RenderAsync(string label, int count)
    {
        await Task.Yield();
        if (count > MaxLabels)
        {
            throw new ArgumentOutOfRangeException(nameof(count));
        }
        string result = prefix;
        for (int index = 0; index < count; index++)
        {
            result += label;
        }
        return result;
    }
}
