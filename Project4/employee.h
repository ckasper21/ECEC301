#ifndef _employee_h_
#define _employee_h_

struct employee {
    char name[128];
    unsigned int age;
    unsigned int wage;
};

unsigned int employee_get_num (struct employee* list);
void employee_print (struct employee* e);
void employee_print_all (struct employee* list);
void employee_sort (struct employee* array);
void employee_add (struct employee* list);
void employee_delete (struct employee* list);

#endif
