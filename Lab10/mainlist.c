#include <stdlib.h>
#include <stdio.h>
#include "list.h"

int main (int argc, char** argv)
{
  struct list* head;
  struct list* item;
  unsigned int i=0;
  head=malloc(sizeof(struct list));
  list_init(head);

  for (i=1;i<=10;i++) {
    item=malloc(sizeof(struct list));
    item->x=i;
    list_add_to_bottom(head,item);
  }
  for (i=0,item=head->next;item!=NULL;item=item->next){
    printf("Item %u: ",i++);
    printf("x=%u\n",item->x);
  }
  printf("Now removing from queue!\n");
  for (i=0, item=list_pop_head(head);item!=NULL;item=list_pop_head(head)){
    printf("Item %u: ",i++);
    printf("x=%u\n",item->x);
    free(item);
  }
  free(head);
  return 0;
}
