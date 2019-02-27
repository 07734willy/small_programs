#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RUNS 100
#define MAX_WIDTH 5000

#define DEBUG
#define COMP

typedef struct {
	char right;
	int index;
	unsigned short x, y, z, w;
	unsigned long value;
} xyz_pack;

unsigned long interleave(unsigned short x, unsigned short y, unsigned short z) {
	unsigned long out = 0;
	for (int i = 0; i < sizeof(x) * 8; i++) {
		out |= (x & 1UL << i) << (2 * i);
		out |= (y & 1UL << i) << (2 * i + 1);
		out |= (z & 1UL << i) << (2 * i + 2);
	}
	return out;
}

int comparator(const void* a, const void* b) {
	unsigned long v1 = ((xyz_pack *) a)->value;
	unsigned long v2 = ((xyz_pack *) b)->value;
	return (v1 - v2);
}

int main() {
	clock_t start, start2, end;

	start = clock();

	srand(time(NULL));

	xyz_pack packs[2*RUNS];
	xyz_pack check[RUNS];

	int i;
	unsigned short x, y, z, w;
	for (i = 0; i < 2*RUNS; i+=2) {
		x = (unsigned short) rand();
		y = (unsigned short) rand();
		z = (unsigned short) rand();
		w = (unsigned short) rand() % MAX_WIDTH;
		
		if (w > x) { w = x; }
		if (w > y) { w = y; }
		if (w > z) { w = z; }

		packs[i].right = 0;
		packs[i+1].right = 1;

		packs[i].index = packs[i+1].index = i;
		packs[i].x = packs[i+1].x = x;
		packs[i].y = packs[i+1].y = y;
		packs[i].z = packs[i+1].z = z;
		packs[i].w = packs[i+1].w = w;
		packs[i].value = interleave(x-w, y-w, z-w);
		packs[i+1].value = interleave(x+w, y+w, z+w);

		check[i/2].index = i;
		check[i/2].x = x;
		check[i/2].y = y;
		check[i/2].z = z;
		check[i/2].w = w;
	}

	qsort((void*) packs, RUNS, sizeof(xyz_pack), comparator);

	start2 = clock();

	int count = 0;

	int idx;
	xyz_pack self, other;
	for (i = 0; i < 2*RUNS; i++) {
		idx = i;
		self = packs[i];

		if (self.right) {
			continue;
		}

		while ((other.index != self.index) && (idx+1 < 2*RUNS)) {
			idx++;
			other = packs[idx];
			if (other.right) {
				continue;
			}
			long radius_sqr = (self.w + other.w) * (self.w + other.w);
			long dist_sqr = 0;
			
			long dx, dy, dz;
			dx = ((long)self.x)-((long)other.x);
			dx *= dx;
			dy = ((long)self.y)-((long)other.y);
			dy *= dy;
			dz = ((long)self.z)-((long)other.z);
			dz *= dz;
			dist_sqr = dx + dy + dz;

			if (dist_sqr < radius_sqr) {
				count++;
				#ifdef DEBUG
				printf("PACK FOUND: %d, %d\n", self.index, other.index);
				printf(" VAL x: %d, %d\n", self.x, other.x);
				printf(" VAL y: %d, %d\n", self.y, other.y);
				printf(" VAL x: %d, %d\n", self.z, other.z);
				printf(" VAL w: %d, %d\n", self.w, other.w);
				#endif
			}

			idx++;
			other = packs[idx];
		}
	}

	printf("Count: %d\n", count);

	end = clock();

	printf("Time: %f\n", ((double)(end-start)) / CLOCKS_PER_SEC);
	printf("Time: %f\n", ((double)(end-start2)) / CLOCKS_PER_SEC);

	//printf("%lu\n", interleave(1<<15,1<<15,1<<15));

	#ifdef COMP
	int alt_count = 0;

	int j;
	for (i = 0; i < RUNS; i++) {
		self = check[i];
		for (j = i + 1; j < RUNS; j++) {
			other = check[j];
			long radius_sqr = (self.w + other.w) * (self.w + other.w);
			long dist_sqr = 0;
			
			long dx, dy, dz;
			dx = ((long)self.x)-((long)other.x);
			dx *= dx;
			dy = ((long)self.y)-((long)other.y);
			dy *= dy;
			dz = ((long)self.z)-((long)other.z);
			dz *= dz;
			dist_sqr = dx + dy + dz;
			
			if (dist_sqr < radius_sqr) {
				alt_count++;
				#ifdef DEBUG
				printf("PACK FOUND: %d, %d\n", self.index, other.index);
				printf(" VAL x: %d, %d\n", self.x, other.x);
				printf(" VAL y: %d, %d\n", self.y, other.y);
				printf(" VAL x: %d, %d\n", self.z, other.z);
				printf(" VAL w: %d, %d\n", self.w, other.w);
				#endif
			}
		}
	}
	
	printf("Alt Count: %d\n", alt_count);
	#endif
}
