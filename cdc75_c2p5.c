#include <stdio.h>
int main(void)
{
  int x=0;
  printf("You are given the following polynomial:\n");
  printf("3x^5+2x^4-5x^3-x^2+7x-6\n");
  printf("Enter a number for x: ");
  scanf("%d",&x);
  printf("The value is %d\n", (3*x*x*x*x*x)+(2*x*x*x*x)-(5*x*x*x)-(x*x)-(7*x)-6);

}
