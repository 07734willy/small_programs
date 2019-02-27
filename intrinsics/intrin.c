#include <stdio.h>
#include <nmmintrin.h>

int main() {
	printf("%d\n", _mm_popcnt_u32(8));
}
