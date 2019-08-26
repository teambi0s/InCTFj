#include <stdlib.h>
#include <stdio.h>

int winner(){
  printf("\nAnd we have a winner folks\n");
  system("/bin/cat flag.txt");
  return 0;
}


int main(int argc, char **argv)
{
  int modified;
  char buffer[44];

  printf("Enter a string : ");
  modified = 0;
  gets(buffer);

  if(modified == 0xcafebabe) {
    winner();
  } else {
    printf("Try again, you got 0x%08x\n", modified);
  }
}
