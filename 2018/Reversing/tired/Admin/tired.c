#include<stdio.h>
#include<string.h>

int main(){
	char inp[34];
	int i;
	printf("Enter a string to get the flag.\n");
	scanf("%s",inp);
	if (strlen(inp)==34){
		char str[]="ch]n`duIbYq[mYnb[nYjl_nnsYnclcha9w";
		if (strcmp(str,inp)==0){
			for (i=0;i<=33;i++){
				str[i]+=6;
			}
			printf("Flag: %s\n",str);
			}
		else 
			printf("Try again\n");
	}
	else 
			printf("Try again\n");
	return 0;
}
