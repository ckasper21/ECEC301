#include <stdio.h>

int main(void)
{
  int gs1,gid,pubcode,itnum,check=0;
  printf("Enter ISBN (XXX-X-XXX-XXXXX-X): ");
  scanf("%d-%d-%d-%d-%d",&gs1,&gid,&pubcode,&itnum,&check);
  printf("GS1 prefix: %d\n",gs1);
  printf("Group identifier: %d\n",gid);
  printf("Publisher code: %d\n",pubcode);
  printf("Item number: %d\n",itnum);
  printf("Check digit: %d\n",check);
  return 0;
}
