#include<stdio.h>
#include<math.h>
#define key "gj]tbfuGtmY_Y-YD/a/tY?nkmtn0jaYjsk^-n{"
#define kez "UoxZl1odZi5oedoZujZbduZuid!cm`b"
int main()
{
int a,i,j,s,n,p;
a = i = j = s = n = p=0;
char k[39];
printf("can you guess the number ??? \n");
scanf("%d",&a);
n=a;
while(n!=0)
	{
	p=n%10;
	s=s+pow(p,3);
	n=n/10;
	}
if(a==s && a!=1)
	{
	for(i=0;i<38;i++)
		{
		k[i]=(((key[i]+3)^3));		
		}	
	k[i]=0;
	printf("%s\n",k);
	}
else 
	{
	for (j=0;j<31;j++)
		{
		k[j]=((kez[j]+2)^3);
		}
		k[j]=0;		
		printf("%s\n",k);
		
	}
return 0 ;
}
	
