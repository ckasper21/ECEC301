#include <stdio.h>
#include "employee.h"
#include <string.h>

unsigned int employee_get_num (struct employee* list)
{
    unsigned int i;
    for (i=0; list[i].name[0]; i++);
    return i;
}

void employee_print (struct employee* e)
{
    printf ("Name: %s\n", e->name);
    printf (" Age: %u\n", e->age);
    printf ("Wage: %u\n", e->wage);
}


void employee_print_all (struct employee* list)
{
  unsigned int i, count;
  count=employee_get_num(list);
  for (i=0;i<count;i++) {
    printf("----------------\n");
    printf("Employee #%u\n",i);
    employee_print(&list[i]);
  }
  printf("----------------\n");
  printf("Num Employees: %u\n",count);
  printf("\n");
}


void employee_sort (struct employee* list)
{
  unsigned int count,i,j;
  struct employee tmp;
  count=employee_get_num(list);
  for (i=0;i<(count-1);i++){
    for (j=0;j<(count-1-i);j++) {
      if (list[j].age > list[j+1].age) {
        tmp=list[j];
        list[j]=list[j+1];
        list[j+1]=tmp;
      }
    }
  }
}


void employee_add (struct employee* list)
{
    unsigned int count;
    char s1[128],s2[128];
    count=employee_get_num(list);
    struct employee tmp;
    printf("First Name: ");
    scanf("%s",&s1[0]);
    printf("Last Name: ");
    scanf("%s",&s2[0]);
    strcat(s1," ");
    strcat(s1,s2);
    strcpy(tmp.name,s1);
    printf("Age: ");
    scanf("%u",&tmp.age);
    printf("Wage: ");
    scanf("%u",&tmp.wage);
    list[0+count]=tmp;
    employee_sort(list);
}


void employee_delete (struct employee* list)
{
  unsigned int count,usr;
  struct employee tmp;
  count=employee_get_num(list);
  printf("Enter ID # to delete: ");
  scanf("%u",&usr);
  if (usr >= count) {
    printf("**Invalid Selection**\n");
    printf("\n");
  } else if (count==1) {
    memset (&list[0],'\0', 1);
    printf("**Employed #%u Deleted**\n",usr);
    printf("\n");
  } else {
    tmp=list[0+count-1];
    list[0+count-1]=list[0+usr];
    list[0+usr]=tmp;
    memset (&list[0+count-1],'\0', 1);
    printf("**Employed #%u Deleted**\n",usr);
    printf("\n");
    employee_sort(list);
  }
}
