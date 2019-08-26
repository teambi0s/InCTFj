#include<stdio.h>

#define OO "khen`}Ch^Y`khcff{Ykn!uYcffYG.njUw"
#define Oo "W(sY_ncYj(lYL`_lYAii<"
#define oO "b;v`sjyf`w;`rn{};yf**"
#define try "W4vv}"

void oOo()
	{
	int i ; 
	char arr[5];
	for (i=0;i<5;i++)
		arr[i]=try[i]^4;
	printf("%s\n",arr);
	}

void OOO()
	{
	int i;
	char arr[34];
	for (i=0;i<33;i++)
		(arr[i]=(((OO[i])+2)^4));
		
	arr[i]=0;
	printf("%s\n",arr);
		
	}

void oOO()
	{
	int i;
	char arr[21];
	for (i=0;i<21;i++)
		(arr[i]=(((oO[i])-6)^5));
	arr[i]=0;	
	printf("%s\n",arr);
		
	}

void OOo()
	{int i;
	char arr[21];
	for (i=0;i<21;i++)
		(arr[i]=(((Oo[i])^3)+5));
		
	arr[i]=0;	
	printf("%s\n",arr);
		
	}


int main()
	{int x;
	int a,b,c;
	printf("Enter 3  numbers\n");
	scanf("%d%d%d",&a,&b,&c);
	if(a*a+b*b<c*c)
		{
		x=0;
		}
	else if(a*a+b*b>c*c)
		{
		x=1;
		}
	else
		{
		x=2;
		}
	if(x%3==0)
		{
		oOo();
		OOo();
		}
	else if(x%3==1)
		{
		oOo();
		oOO();
		}
		
	else
		{
		OOO();
		}
	return 0;
	
	}
	
