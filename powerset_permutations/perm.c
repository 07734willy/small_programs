#include <stdio.h>
#include <string.h>

void swap(char* arr, int i, int j) {
	char t = arr[i];
	arr[i] = arr[j];
	arr[j] = t;
}

void permute(char *str, int i, int n) {
	for (int j = i; j < n; j++) {
		swap(str, i, j);
		if (!str[i]) {
			printf("%s\n", str);
		} else {
			permute(str, i+1, n);
		}
		swap(str, i, j); 
	}
} 

int main(void) {
    char str[] = "1234";
	permute(str, 0, strlen(str) + 1);
}
