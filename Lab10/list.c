#include <stdio.h>
#include "list.h"

void list_init(struct list* head)
{
  head->next= NULL;
}

void list_add_to_bottom(struct list* head, struct list* new_item)
{
  struct list* tmp=head;

  while (tmp->next) {
    tmp=tmp->next;
  }
  new_item->next=NULL;
  tmp->next=new_item;
}

struct list* list_pop_head(struct list* head)
{
  struct list* item;
  item=head->next;
  if (item!=NULL){
    head->next=item->next;
    item->next=NULL;
  }
  return item;
}
