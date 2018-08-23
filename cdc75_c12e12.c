#include <stdio.h>

void find_two_largest(const int *a, int n, int *largest, int *second_largest)
{
  int *p;

  if (*a>*(a+1)){
    *largest=*a;
    *second_largest=*(a+1);
  } else {
    *largest=*(a+1);
    *second_largest=*a;
  }
  for (p=a+2; p<(a+n);p++){
    if (*p>*largest){
      *second_largest=*largest;
      *largest=*p;
    } else if (*p>*second_largest){
      *second_largest=*p;
    }
  }
}

int main(void)
{
int *largest_p,*second_largest_p;
int n=5,largest,second_largest;
int a[5]={2,5,10,3,6};
int *a_p=a;
largest_p=&largest;
second_largest_p=&second_largest;

find_two_largest(a_p,n,largest_p,second_largest_p);
printf("Largest number: %i\n",*largest_p);
printf("Second largest number: %i\n",*second_largest_p);
}
