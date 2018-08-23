#include <stdio.h>

int main (void)
{
  float input,duetax;
  int dec=2;
  printf("Enter taxable income ($xxxx.xx): ");
  scanf("$%f",&input);

  if (input<750){
    duetax=0.01*input;
  } else if (input>=750 && input<2250) {
    duetax=7.5+(input*0.02);
  } else if (input>=2250 && input<3750) {
    duetax=37.5+(input*0.03);
  } else if (input>=3750 && input<5250) {
    duetax=82.5+(input*0.04);
  } else if (input>=5250 && input<7000) {
    duetax=142.5+(input*0.05);
  } else if (input>=7000) {
    duetax=230+(input*0.06);
  }
  printf("Tax due: $%.*f\n",dec,duetax);
}
