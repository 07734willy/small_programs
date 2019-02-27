#include <unistd.h>

int main(int argc, char** argv) {
	long i;
	int stress = 10;
	while (1) {
		for (i = 0; i < (1L << stress); i++) { }
		usleep(1);
	}
}
