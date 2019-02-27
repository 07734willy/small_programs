#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct flag {
	int8_t (*valid)(struct flag* flags);
	const uint8_t requiresValue;
	const char* name;
	uint8_t active;
	char* value;
} Flag;


int8_t fun(Flag flags[]) {
	printf("hello world\n");
}


int main() {
	Flag f;
	f.valid = fun;
	f.valid(&f);
	return 0;
}
