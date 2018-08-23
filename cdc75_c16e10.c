#include <stdio.h>

struct point {
  int x;
  int y;
};

struct rectangle {
  struct point upperleft;
  struct point lowerright;
};

int area_rect (struct rectangle* r)
{
  int len,wid;
  len=(r->lowerright.x)-(r->upperleft.x);
  wid=(r->upperleft.y)-(r->lowerright.y);
  return len*wid;
}

struct point center_rect (struct rectangle* r)
{
  struct point cent;
  cent.x=((r->lowerright.x)+(r->upperleft.x))/2;
  cent.y=((r->upperleft.y)+(r->lowerright.y))/2;
  return cent;
}

void move_rect (struct rectangle* r, int x, int y)
{
  r->upperleft.x=r->upperleft.x+x;
  r->upperleft.y=r->upperleft.y+y;
  r->lowerright.x=r->lowerright.x+x;
  r->lowerright.y=r->lowerright.y+y;
}

int inside_rect (struct rectangle* r, struct point* p)
{
  if ((p->x >= r->upperleft.x) && (p->x <= r->lowerright.x)
      && (p->y <= r->upperleft.y) && (p->y >= r->lowerright.y)) {
        return 1;
      }
  return 0;
}

int main(void)
{
  struct point p1,p2,center,p3;
  p1.x=2;
  p1.y=4;
  p2.x=4;
  p2.y=2;
  struct rectangle r;
  r.upperleft=p1;
  r.lowerright=p2;
  printf("Corners of r are (%i,%i) and (%i,%i)\n",r.upperleft.x,
                              r.upperleft.y,r.lowerright.x,r.lowerright.y);
  printf("The area of r is %i\n",area_rect(&r));
  center=center_rect(&r);
  printf("The center of r is (%i,%i)\n",center.x,center.y);
  p3.x=1;
  p3.y=1;
  printf("New p3 is (%i,%i)\n",p3.x,p3.y);
  if (inside_rect(&r,&p3)){
    printf("p3 lies within r\n");
  } else {
    printf("p3 is not within r\n");
  }
  printf("Moving r so lowerleft corner is at (0,0)\n");
  move_rect(&r,-2,-2);
  if (inside_rect(&r,&p3)){
    printf("p3 now lies within r\n");
  } else {
    printf("p3 is now within r\n");
  }
}
