#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *getFlag(char *a,char *b,char *c,char *d,int mod)
{
    int la,lb,lc,ld ;
    la = strlen(a) ;
    lb = strlen(b) ;
    lc = strlen(c) ;
    ld = strlen(d) ;
    int lens[4] = {la,lb,lc,ld} ;
    int n = la+lb+lc+ld ;
    int i = 0;
    char *eFlag = (char*) malloc((la+lb+lc+ld+1)*sizeof(char)) ;
    int b_off = (mod*5)%3 ;
    int c_off = (mod*7)%3 ;
    int d_off = (mod*8)%3 ; 
    for(i=0;i<la;i+=1)
        a[i] -= lens[i%4] ;
    for(i=0;i<lb;i+=1)
        b[i] -= lens[(i+mod*5)%4] + b_off ;
    for(i=0;i<lc;i+=1)
        c[i] -= lens[(i+mod*3)%4] + c_off ;
    for(i=0;i<ld;i+=1)
        d[i] -= lens[(i+mod*5)%4] + d_off ;
    if(eFlag==NULL)
        return "Well That Seems Superfluos\n" ;
    strcpy(eFlag,a) ;
    strcat(eFlag,b) ;
    strcat(eFlag,c) ;
    strcat(eFlag,d) ;
    eFlag[n] = 0 ;
    return eFlag ;
}

void main() 
{
    char a[9] = {113, 104, 110, 116, 103, 113, 114, 131,0} ;
    char b[4] = {104, 134, 97,0} ;
    char c[10] = {68, 124, 57, 97, 127, 91, 72, 105, 114,0} ;
    char d[16] = {122, 81, 119, 61, 119, 106, 128, 96, 56, 125, 87, 118, 53, 98, 142,0} ;
    char name[32] ;
    char login = 0 ;
    char pass[32] ;
    
    printf("%#x %#x \n",pass+32,&login) ;
    printf("User : ") ;
    fgets(name,32,stdin) ;
    printf("Password : ") ;
    gets(pass) ;
    if(login)
    {
        printf("Access Granted !\n") ;
        printf("%s\n",getFlag(a,b,c,d,1)) ;
    }
    else
    {
        printf("Access Denied\n") ;
    }
    
}