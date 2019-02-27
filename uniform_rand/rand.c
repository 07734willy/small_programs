#include <stdio.h>
#include <stdlib.h>

int u_rand(int min, int max) {
	int threshold = RAND_MAX - RAND_MAX % (max - min);
	int num = rand();
	while (num >= threshold) {
		num = rand();
	}
	return num % (max - min) + min;
}

int main() {
	int i;
	for (i = 0; i < 20; i++) {
		printf("%d\n", u_rand(3, 6));
	}
}
