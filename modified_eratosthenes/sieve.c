#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int sieve(int N, unsigned int* lp, unsigned int* pr) {
	int pr_size = 0;
	for (int i=2; i<=N; ++i) {
		if (lp[i] == 0) {
			lp[i] = i;
			pr[pr_size++] = i;
		}
		for (int j=0; j<pr_size && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
			lp[i * pr[j]] = pr[j];
	}
	return pr_size;
}

int sieve2(int N, unsigned int* lp, unsigned int* pr) {
	int pr_size = 0;
	for (int i=2; i < N; ++i) {
		if (lp[i] != 0) {
			pr[pr_size++] = i;
		}
		int j = i;
		while (j * i < N) {
			lp[j * i] = 0;
			j += lp[j];
		}
	}
	return pr_size;
}

int main() {
	const int N = 100;
	unsigned int* lp = calloc(N, sizeof(unsigned int));
	unsigned int* pr = calloc(N, sizeof(unsigned int));
	
	unsigned int* lp2 = malloc(N * sizeof(unsigned int));
	unsigned int* pr2 = calloc(N, sizeof(unsigned int));
	memset(lp2, 1, N * sizeof(unsigned int)); 
	
	int pr_len  = sieve(N, lp, pr);
	int pr_len2 = sieve2(N, lp2, pr2);

	int i;
	for (i = 0; i < pr_len2; i++) {
		printf("%u\n", pr2[i]);
	}
}
