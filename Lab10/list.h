#ifndef _list_h_
#define _list_h_

struct list {
  unsigned int x;
  struct list* next;
};

void list_init(struct list* head);
void list_add_to_bottom(struct list* head, struct list* new_item);
struct list* list_pop_head(struct list* head);

#endif
