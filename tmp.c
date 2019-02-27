    #include <stdio.h>
	#include <stdlib.h>
    #include <time.h>
    #include <math.h>

    float FastInvSqrt (float number);

    int
    main ()
    {
      float x = 10.0;

      int N = 100000001;
	  int* arr = malloc(sizeof(int) * N);
      int i = 0;
	  for (i = 0; i < N; i++) {
	  	arr[i] = rand();
	}

      clock_t start2 = clock (); 
	  volatile float z = 0;
      do  
        {   
          z += 1.0 / sqrt (arr[i]+z);
          i++;
        }   
      while (i < N); 
      clock_t end2 = clock (); 

		printf("%f\n", z);
      double time2 = (end2 - start2) / (double) CLOCKS_PER_SEC;

      printf ("1/sqrt() spends %13f sec.\n\n", time2);

		x = 10.0;
      i = 0;
      clock_t start1 = clock (); 
      do  
        {   
          z += FastInvSqrt (arr[i]+z);
          i++;
        }   
      while (i < N); 
      clock_t end1 = clock (); 

		printf("%f\n", z);
      double time1 = (end1 - start1) / (double) CLOCKS_PER_SEC;



      printf ("FastInvSqrt() spends %f sec.\n\n", time1);


      printf ("fast inverse square root is faster %f times than 1/sqrt().\n", time2/time1);

      return 0;
}

float
FastInvSqrt (float x)
{
  float xhalf = 0.5F * x;
  int i = *(int *) &x;  // store floating-point bits in integer
  i = 0x5f3759df - (i >> 1);    // initial guess for Newton's method
  x = *(float *) &i;            // convert new bits into float
  x = x * (1.5 - xhalf * x * x);        // One round of Newton's method
  //x = x * (1.5 - xhalf * x * x);      // One round of Newton's method
  //x = x * (1.5 - xhalf * x * x);      // One round of Newton's method
  //x = x * (1.5 - xhalf * x * x);      // One round of Newton's method
  return x;
}
