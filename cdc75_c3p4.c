#include <stdio.h>

int main(void)
{
  int nums1,nums2,nums3=0;
  printf("Enter phone number [(xxx) xxx-xxxx]: ");
  scanf("(%d) %d-%d",&nums1,&nums2,&nums3);
  printf("You entered %d.%d.%d\n",nums1,nums2,nums3);
  return 0;
}
