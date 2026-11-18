#define SAMPLE_LIMIT 4

typedef struct Sample {
    int value;
    unsigned count;
} Sample;

int sample_total(Sample sample) {
    int total = 0;
    for (unsigned index = 0; index < sample.count; index++) {
        if (index < SAMPLE_LIMIT) {
            total += sample.value;
        }
    }
    return total;
}
