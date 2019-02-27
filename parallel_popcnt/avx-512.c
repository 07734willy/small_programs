#include <immintrin.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  const unsigned long knl_features =
      (_FEATURE_AVX512F | _FEATURE_AVX512ER |
       _FEATURE_AVX512PF | _FEATURE_AVX512CD );
  if ( _may_i_use_cpu_feature( knl_features ) )
    printf("This CPU supports AVX-512F+CD+ER+PF as introduced in Knights Landing\n");
  else
    printf("This CPU does not support all Knights Landing AVX-512 features\n");
  return 1;
}

