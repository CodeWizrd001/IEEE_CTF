#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char *s = "HuR4" ;
	char *sn = "K3n" ;
	char *mypass = (char *) calloc(50,sizeof(char)) ;
	char *pass = (char *) calloc(100,sizeof(char)) ;
	strcat(mypass,s) ;
	strcat(mypass,sn) ;
	printf("Enter Password : ") ;
	scanf("%s",pass) ;
	if(!strcmp(mypass,pass)) 
	{
		printf("[+] Access Granted\n") ;
		printf("ieee_nitc{B1N4rY_flAG_101}\n") ;
	}
	else 
		printf("[-] Access Denied\n") ;
}
