#include <stdio.h>

#define LEN 3

int sum_two_dimensional_array(const int a[][LEN], int n)
{
  const int *a_p;
  int sum=0;

  for (a_p=&a[0][0];a_p<=&a[n-1][LEN-1];a_p++){
    sum+=*a_p;
  }
  return sum;
}


int main(void)
{
int sum=0,n=4;
/* n is the number of rows */
int a[4][3]=
{
  {1,2,3},
  {4,5,6},
  {7,8,9},
  {10,11,12},
};
printf("array a =\n");
printf("{1,2,3}\n{4,5,6}\n{7,8,9}\n{10,11,12}\n");
sum=sum_two_dimensional_array(a,n);
printf("The sum of the array is: %i\n",sum);
}
