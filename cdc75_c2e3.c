#include <stdio.h>
int main(void)
{
  int height,length,width,volume=0;
  printf("Enter height of box: ");
  scanf("%d", &height);
  printf("Enter length of box: ");
  scanf("%d", &length);
  printf("Enter width of box: ");
  scanf("%d", &width);
  volume=height*length*width;

  printf("Volume (cubic inches): %d\n",volume);
  printf("Dimensional weight (pounds): %d\n", ((volume+165)/166));
  return 0;
}
