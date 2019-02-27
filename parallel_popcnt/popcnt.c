#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

int add(uint8_t* a, int s1, uint8_t* b, int s2, uint8_t* carry) {
	int len = s1 < s2 ? s2 : s1;
	//uint8_t* carry = calloc(len + 1, sizeof(uint8_t));
	int i;
	for (i = 0; i < len; i++) {
		carry[i] = a[i] & b[i];
		a[i] ^= b[i];
	}
	a[len] = 0;
	for (i = 0; i < len; i++) {
		carry[i+1] |= a[i+1] & carry[i];
		a[i+1] ^= carry[i];
	}
	if (a[len]) {
		len++;
	}
	return len;
}

int sum(uint8_t* arr, int size) {
	uint8_t* carry = calloc(size + 1, sizeof(uint8_t));
	int i;
	for (i = 1; i < size; i <<= 1) {
		int j;
		for (j = 0; j < size; j += 2 * i) {
			add(arr + j, i, arr + j + i, i, carry);
		}
	}
	return 0;
}

void sum2(uint8_t* arr, int size) {
	uint32_t* counts = calloc(size, sizeof(uint32_t));
	while (size > 0) {
		int i;
		uint8_t c[8] = {0, 0, 0, 0, 0, 0, 0, 0};
		for (i = 0; i < 255; i++) {
			int j;
			for (j = 0; j < 8; j++) {
				c[j] += (arr[i] >> j) & 1;
			}
		}
		int j;
		for (j = 0; j < 8; j++) {
			counts[j] += c[j];
		}
		size -= 255;
	
	}
	if (counts[0] == -1) {
		exit(0);
	}
}

#define TESTSIZE 100000

int main() {
	uint8_t arr[4] = {0x53, 0xAD, 0x46, 0xA9};
	//uint8_t* carry = calloc(5, sizeof(uint8_t));
	//add(arr, 2, arr + 2, 2, carry);
	/*sum(arr, 4);
	int i;
	for (i = 0; i < 4; i++) {
		printf("%u\n", arr[i]);
	}*/
	clock_t start, end;
	uint8_t* testarr = malloc(TESTSIZE * sizeof(uint8_t));
	int i;
	for (i = 0; i < TESTSIZE; i++) {
		testarr[i] = (uint8_t)rand();
	}
	start = clock();
	sum2(testarr, TESTSIZE);
	end = clock();
	printf("Duration: %f\n", ((double)(end-start)/CLOCKS_PER_SEC));
	start = clock();
	sum(testarr, TESTSIZE);
	end = clock();
	printf("Duration: %f\n", ((double)(end-start)/CLOCKS_PER_SEC));
}





















