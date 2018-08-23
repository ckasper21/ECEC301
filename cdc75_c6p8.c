#include <stdio.h>

int main (void) {

int numdays,startday,i,j,count;

printf("Enter the number of days in month: ");
scanf("%i",&numdays);
printf("Enter starting day of the week (1=Sun,7=Sat): ");
scanf("%i",&startday);

for (j=1;j<startday;j++){
  printf("   ");
}
count=startday-1;
for (i=1;i<=numdays;i++) {
  if (i < 10) {
    printf(" %i ",i);
    count++;
    if (count==7) {
      printf("\n");
      count=0;
    }

  } else {
    printf("%i ",i);
    count++;
    if (count==7) {
      printf("\n");
      count=0;
    }
    if (i==numdays){
      printf("\n");
    }
    }
}
}
