#include <stdio.h>

void store_zeros(int a[], int n)
{
  /* remove i and all instances of [] operator*/
  int *p;
  for (p=a;p<=a+n;p++){
    *p=0;
  }
}

int main(void)
{
int i,n=5;
int a[5]={1,2,3,4,5};
printf("Before Function\n");
for (i=0;i<n;i++){
  printf("a[%i]=%i\n",i,a[i]);
}
printf("After Function\n");
store_zeros(a,n);
for (i=0;i<n;i++){
  printf("a[%i]=%i\n",i,a[i]);
}
}
