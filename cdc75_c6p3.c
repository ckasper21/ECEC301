#include <stdio.h>

int main (void) {
int num,den,gcd,i;

printf("Enter a fraction (x/x): ");
scanf("%i/%i",&num,&den);

for (i=1; i<=num && i<=den;i++){
  if (num%i==0 && den%i==0) {
    gcd=i;
  }
  }
printf("In lowest terms: %i/%i\n",(num/gcd),(den/gcd));
}
