#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	int size = 10000;
	char** array1 = malloc(size * sizeof(char*));
	int i;
	for (i = 0; i < size; i++) {
		array1[i] = malloc(size*sizeof(char));
	}

	clock_t start, end;
	start = clock();

	for (i = 0; i < size; i++) {
		int j;
		//__builtin_prefetch(array1[0] + i, 1, 1);
		for (j = 0; j < size; j++) {
			//__builtin_prefetch(array1[j+1] + i, 1, 1);
			array1[j][i] = 1;
		}
	}
	

	end = clock();
	printf("Time used: %f\n", ((double) end - start) / CLOCKS_PER_SEC);
}
