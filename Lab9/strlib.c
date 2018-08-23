#include <stdio.h>
#include "strlib.h"

int my_strlen(char* string)
{
  int count=0,i;
  for (i=0;string[i]!='\0';i++){
    count++;
  }
  return count;
}

int my_strcmp(char* a, char* b)
{
  int i;
  for (i=0;(a[i]!='\0')||(b[i]!='\0');i++){
    if (a[i]!=b[i]){
      return 1;
    }
  }
  return 0;
}
