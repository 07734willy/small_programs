#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <immintrin.h>
#include <time.h>

uint32_t* pop1(uint8_t* arr, int columns, int rows) {
	uint32_t* counts = calloc(columns, sizeof(uint32_t));
	int i;
	for (i = 0; i < rows; i++) {
		int j;
		for (j = 0; j < columns / CHAR_BIT; j++) {
			int k;
			for (k = 0; k < CHAR_BIT; k++) {
				counts[k + j * CHAR_BIT] += (arr[j + i * columns / CHAR_BIT] >> (7 - k)) & 1;
			}
		}
	}
	return counts;
}

uint32_t* pop2(uint8_t* arr, int columns, int rows) {
	uint32_t* counts = calloc(columns, sizeof(uint32_t));
	__m256i* subcnt = aligned_alloc(256, columns * sizeof(__m256i));
	__m256i* masks = aligned_alloc(256, CHAR_BIT * sizeof(__m256i));
	int i;
	printf("d\n");
	for (i = 0; i < columns; i++) {
		subcnt[i] = _mm256_setzero_si256();
	}
	for (i = 0; i < 8; i++) {
		masks[i] = _mm256_set1_epi8(1 << i);
	}
	for (i = 0; i < rows; i++) {
		int j;
		for (j = 0; j < columns / 256; j++) {
			__m256i val = _mm256_load_si256((__m256i*)(arr + j * 256 / CHAR_BIT + i * columns / CHAR_BIT));
			int k;
			for (k = 0; k < CHAR_BIT; k++) {
				subcnt[k] = _mm256_add_epi8(subcnt[k], _mm256_and_si256(val, masks[k]));
			}
		}
	}
}
#define TEST_ROWS 10000
#define TEST_COLS 512

int main() {
	uint8_t* tests = aligned_alloc(256,TEST_ROWS * TEST_COLS * sizeof(uint8_t));
	int i;
	for (i = 0; i < TEST_ROWS * TEST_COLS; i++) {
		tests[i] = (uint8_t) rand();
	}

	clock_t start, end;

	start = clock();
	uint32_t* res1 = pop1(tests, TEST_COLS, TEST_ROWS);
	end = clock();
	printf("Duration: %f\n", ((double)(end-start)/CLOCKS_PER_SEC));
	start = clock();
	uint32_t* res2 = pop2(tests, TEST_COLS, TEST_ROWS);
	end = clock();
	printf("Duration: %f\n", ((double)(end-start)/CLOCKS_PER_SEC));

	/*
	for (i = 0; i < TEST_COLS; i++) {
		printf("%u\n", res1[i]);
	}*/
}
