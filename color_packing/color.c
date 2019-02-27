#include <stdio.h>
#include <stdlib.h>

#define min(x, y) (x <= y ? x : y)

typedef unsigned int color_t;
typedef unsigned char channel_t;

static channel_t add_saturate_channel(channel_t a, channel_t b) {
	return min((color_t)a+(color_t)b, (channel_t)255);
}


static color_t add_saturate(color_t a, color_t b) {
	return (
		add_saturate_channel(a       & 0xff, b       & 0xff)
		| add_saturate_channel(a >>  8 & 0xff, b >>  8 & 0xff) <<  8
		| add_saturate_channel(a >> 16 & 0xff, b >> 16 & 0xff) << 16
		| add_saturate_channel(a >> 24 & 0xff, b >> 24 & 0xff) << 24
	);
}

static color_t mix_50_50(color_t a, color_t b) {
	return (((a ^ b) >> 1  &  0x7f7f7f7f) + (a & b));
}

static color_t add_saturate2(color_t a, color_t b) {
	return (
		((mix_50_50(a, b) & 0x80808080) >> 7) * 0xFF
		| (((mix_50_50(a, b) & 0x7f7f7f7f) << 1))
		| ((a ^ b) & 0x01010101)
	);
}

static color_t masked_mix(color_t a, color_t b) {
	return (((a ^ b) & 0xFEFEFEFE) + ((a & b) << 1)) & 0x01010101;
}

static color_t add_saturate3(color_t a, color_t b) {
	return (
		((mix_50_50(a, b) & 0x80808080) >> 7) * 0xFF
		//| (mix_50_50_2(a, b) & 0xFEFEFEFE)
		| ((a ^ b) & 0x01010101)
	);
}

static color_t add_saturate4(color_t a, color_t b) {
	return (
		masked_mix(a, b) * 0xFF >> 8
		| (a + b - masked_mix(a, b))
	);
}

static color_t add_saturate5(color_t a, color_t b) {
	color_t s = a + b;
	color_t m = (s - ((a ^ b) & 0x01010101)) & 0x01010101;
	return m * 0xFF >> 8 | (s - m);
}

static color_t add_saturate6(color_t a, color_t b) {
	color_t s = ((a + b) - ((a ^ b) & 0x01010101)) & 0x01010101;
	return s * 0xFF >> 8 | (a + b - s);
}

static color_t add_saturate7(color_t a, color_t b) {
    color_t s = a + b;
    color_t m = (s - ((a ^ b) & 0x01010101)) & 0x01010101;
    return (m >> 8 | m << 24) * 0xff | (s - m);
};

static color_t add_saturate_a(color_t a, color_t b) {
    color_t s = a + b;
    color_t m = (s - ((a ^ b) & 0x01010100)) & 0x01010100;
    return (m >> 8 | 0x01000000 * (s < a)) * 0xff | (s - m);
};

int main(int argc, char** argv) {
	int i;
	for (i = 0; i < 10000000; i++) {
		color_t a = rand() & 0xFFFFFFFF;
		color_t b = rand() & 0xFFFFFFFF;
		if ((add_saturate_a(a, b) != add_saturate7(a, b)) || (add_saturate(a, b) != add_saturate7(a, b))) {
			printf("%x %x\n", a, b);
			printf("  %x\n  %x\n  %x\n", add_saturate(a, b), add_saturate7(a, b), add_saturate_a(a, b));
		}
	}
}
