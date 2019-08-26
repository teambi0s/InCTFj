#include<stdio.h>
#include<stdlib.h>

/*  0xdec0ded */

int winner(){
  printf("\nYou earn a flag.\n");
  system("/bin/cat flag.txt");
  return 0;
}


int main()
{
  int number_1  = 286330349;
  int number_2  = 233570577;

  int magic_number;

  ((char *)&magic_number)[1] = ((char *)&number_1)[1];
  ((char *)&magic_number)[3] = ((char *)&number_2)[3];
  ((char *)&magic_number)[0] = ((char *)&number_1)[0];
  ((char *)&magic_number)[2] = ((char *)&number_2)[2];

  int num;
  printf("Enter the magic number : ");
  scanf("%d",&num);

  if(num==magic_number)
           winner();
         else
           printf("Nope.\nTry again ?\n");

  return 0;
}
