#include <stdio.h>

int main(int argc, char** argv) {
	unsigned int length = 4;
	unsigned int array[4] = {0, 0, 0, 0};
	
	int i, j;
	for (i = 0; i < 1 << length; i++) {
		array[__builtin_ctz(i)] ^= 1;
		
		printf("Array Values: ");
		for (j = 0; j < length; j++) {
			printf("%d ", array[j]);
		}
		printf("\n");
	}
	return 0;
}
