#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char *pass = (char *) calloc(100,sizeof(char)) ;
	char *flag = (char *) calloc(50,sizeof(char)) ;
	strcpy(flag,"jijodwmvj~_4~geU9iN8KbUi8\\~") ;
	int c[] = {1, 4, 5, 10, 5, 9, 4, 2, 7, 3, 6, 4, 9, 8, 2, 3, 5, 6, 3, 5, 7, 3, 1, 1, 4, 8, 1} ;
	printf("Enter Password : ") ;
	scanf("%s",pass) ;
	if(!strcmp(pass,"iM4GiNeThat")) 
	{
		printf("[+] Access Granted\n") ;
		for(int i=0;i<27;i+=1)
			flag[i] -= c[i] ;
		printf("%s\n",flag) ;
	}
	else 
		printf("[-] Access Denied\n") ;
}
