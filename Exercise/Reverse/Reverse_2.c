#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *encode(char *pass) 
{
	char *npass = (char*) calloc(100,sizeof(char)) ;
	int n = strlen(pass) ;
	for(int i = 0 ; i < n ; i+=1)
		npass[i] = pass[i]+i%3 ;
	return npass ;
}

char *decode(char *pass) 
{
	char *npass = (char*) calloc(100,sizeof(char)) ;
	int n = strlen(pass) ;
	for(int i = 0 ; i < n ; i+=1)
		npass[i] = pass[i]-i%3 ;
	return npass ;
}

void main(int argc,char **argv)
{
	char *user = calloc(100,sizeof(char)) ;
	char *pass = calloc(100,sizeof(char)) ;
	char *flag = calloc(100,sizeof(char)) ;
	char *upss = calloc(100,sizeof(char)) ;

	strcpy(flag,"ifge`piue") ;
	strcat(flag,"{JaW1pDfT") ;
	strcat(flag,"_Xjy`5}") ;

	printf("/'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\\\n") ;
	printf("|			Welcome friend 					|\n") ;
	printf("\\_______________________________________________________________________/\n") ;
	if(argc<3) 
	{
		printf("[!] Error ! User Credentials Missing !\n") ;
		exit(0) ;
	}
	if(argc==3)
	{
		printf("[+] Authenticating \n") ;
		if(strcmp("Dr4G0Kn1te",argv[1]))
		{
			printf("[!] Error ! Invalid Username !\n") ;
			exit(0) ;
		}
		else
		{
			pass = encode(argv[2]) ;
			if(strcmp("P575Xqre2012",pass))
			{
				printf("[!] Error ! Invalid Password !\n") ;
				exit(0) ;
			}
			else 
			{
				printf("[+] Access Granted !\n") ;
				printf("%s\n",decode(flag)) ;
			}
		}
	}


}
