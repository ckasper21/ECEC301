#include <stdlib.h>
#include <stdio.h>
#include "mymath.h"

int main (int argc, char** argv) {

  unsigned int num,i;
  unsigned long* elements;

  if (argc==2){
    num=atoi(argv[1]);
  } else {
      printf ("Usage: %s some_integer\n", argv[0]);
      return 1;
  }

  elements=malloc(num* sizeof(long));
  compute_fibs (elements, &num);

  for (i=0; i<num; i++) {
    printf ("fibs[%i]: %lu\n", i, elements[i]);
  }
  printf ("Displaying %u fibs\n", num);
  free(elements);

}
