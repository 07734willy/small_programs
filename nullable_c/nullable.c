#include<stdio.h>
#include<stdlib.h>

// Value of uninitialized
#define NOTHING 0
// Convert from MaybeType to Type
#define SOME(x) x.value
// Check if whether MaybeType is Nothing (handle cases elsewhere)
#define MATCH(x) !!x.init
// Keep as MaybeType, but set to a non-Nothing value
#define LET(x, y) do { x.value = y; x.init = 1; } while (0)

typedef struct {
  char init;
  int value;
} MaybeInt;

int main(){
  MaybeInt arr[12] = {{NOTHING, 0}};
  int i;

  LET(arr[0], 1);
  LET(arr[1], 2);
  LET(arr[2], 3);
  LET(arr[4], 5);

  for(i = 0; i<12;i++){
      if(!MATCH(arr[i])) {
        printf("Null\n");
      } else {
        printf(" %d\n",SOME(arr[i]));
      }
   }
}
