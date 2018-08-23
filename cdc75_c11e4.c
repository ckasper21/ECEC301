#include <stdio.h>

void swap(int *p, int *q)
{
int temp;
temp=*p;
*p=*q, *q=temp;
}

int main(void)
{
int p,q;
printf("Enter a number for p: ");
scanf("%i",&p);
printf("Enter a number for q: ");
scanf("%i",&q);
printf("SWAP\n");

swap(&p,&q);

printf("p is now %i and q is now %i\n",p,q);

}
