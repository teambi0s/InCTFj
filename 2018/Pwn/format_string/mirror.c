#include <stdio.h>
char FLAG[]="inctf{fake_flag}";

int main()
{
  char * flag = FLAG;
  char buffer[0x20];
  scanf("%31s",buffer);
  printf(buffer);
}
  
