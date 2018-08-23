#include <stdio.h>

struct fraction {
    int num;
    int den;
  };

  void simp(struct fraction* a)
  {
    int gcd,i;
    for (i=1; i<=(a->num) && i<=(a->den);i++){
      if (a->num%i==0 && a->den%i==0) {
        gcd=i;
      }
    }
    a->num=(a->num/gcd);
    a->den=(a->den/gcd);
  }

  void add(struct fraction* a, struct fraction* b)
  {
    struct fraction f;
    if (a->den==b->den){
      f.num=(a->num)+(b->num);
      f.den=(a->den);
    } else {
      f.num=(a->num)*(b->den)+(b->num)*(a->den);
      f.den=(a->den)*(b->den);
    }
    simp(&f);
    printf("%i/%i\n",(f.num),(f.den));
  }

  void sub(struct fraction* a, struct fraction* b)
  {
    struct fraction f;
    if (a->den==b->den){
      f.num=(a->num)-(b->num);
      f.den=(a->den);
    } else {
      f.num=(a->num)*(b->den)-(b->num)*(a->den);
      f.den=(a->den)*(b->den);
    }
    simp(&f);
    printf("%i/%i\n",(f.num),(f.den));
  }

  void mult(struct fraction* a, struct fraction* b)
  {
    int n,d;
    struct fraction f;
    f.num=(a->num)*(b->num);
    f.den=(a->den)*(b->den);
    simp(&f);
    printf("%i/%i\n",(f.num),(f.den));

  }

  void div(struct fraction* a, struct fraction* b)
  {
    int n,d;
    struct fraction f;
    f.num=(a->num)*(b->den);
    f.den=(a->den)*(b->num);
    simp(&f);
    printf("%i/%i\n",(f.num),(f.den));
  }

  int main (void)
  {
    struct fraction f1,f2;
    f1.num=2;
    f1.den=4;
    printf("f1: %i/%i\n",f1.num,f1.den);
    f2.num=3;
    f2.den=9;
    printf("f2: %i/%i\n",f2.num,f2.den);
    simp(&f1);
    simp(&f2);
    printf("f1 simplified is %i/%i\n",f1.num,f1.den);
    printf("f2 simplified is %i/%i\n",f2.num,f2.den);
    printf("f1+f2= ");
    add(&f1,&f2);
    printf("f1-f2= ");
    sub(&f1,&f2);
    printf("f1*f2= ");
    mult(&f1,&f2);
    printf("f1/f2= ");
    div(&f1,&f2);
  }
