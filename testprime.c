 #include <stdio.h>

int is_prime (int n)
{
  int d;
  for (d = 2; (d*d)<=n; d++) {
      if (!(n % d))
        return 0;
  }
  return 1;
}

int main (int argc, char** argv)
{
  int num,i,count;

  if (argc==2){
    num=atoi(argv[1]);
  } else {
      printf ("Usage: %s some_integer\n", argv[0]);
      return 1;
    }

  for (count=0,i=2; count<(num); i++){
    if (is_prime(i)){
      printf("%u\n",i);
      count++;
    }
  }
}
