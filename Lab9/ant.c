#include <stdio.h>
#include "ant.h"

void init_ant (struct ant* a, int position)
{
  a->position=position;
  a->direction=1;
}

void ant_turn (struct ant* a)
{
  a->direction=!(a->direction);
}

void ant_move (struct ant* a, unsigned int distance)
{
  if (a->direction==1) {
    a->position=a->position+distance;
  } else if (a->direction==0){
    a->position=a->position-distance;
  }
}

int ant_get_position (struct ant* a)
{
  return a->position;
}

char* ant_get_direction (struct ant* a)
{
  if (a->direction==1){
    return "Right";
  } else {
    return "Left";
  }
}
