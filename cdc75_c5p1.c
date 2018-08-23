#include <stdio.h>

int main (void)
{
  int input,temp;
  printf("Enter a number: ");
  scanf("%i",&input);
  temp=input;
  if (input<0){
    temp=input-(input*2);
  }

    if (temp>=0 && temp<=9){
    printf("The number %i has 1 digit\n", input);
  } else if (temp>=10 && temp<=99){
    printf("The number %i has 2 digits\n", input);
  } else if (temp>=100 && temp<=999){
    printf("The number %i has 3 digits\n", input);
  } else if (temp>=1000 && temp<=9999){
    printf("The number %i has 4 digits\n", input);
  } else {
    printf("Number is too big!\n");
  }
}
