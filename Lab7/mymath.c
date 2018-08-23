#include <stdio.h>
#include <limits.h>

void compute_fibs (unsigned long* fibs, unsigned int* N)
{
unsigned long int a=0, b=1, i;

for (i=0; i<*N; i++) {
  if ((ULONG_MAX-b)<a){
    *N=i;
    break;
  }
  if (i<=1) {
    fibs[i]=i;
  } else {
    fibs[i]=a+b;
    a=b;
    b=fibs[i];
    }
  }
}
