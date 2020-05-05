#include <stdio.h>
#include <stdlib.h>
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
        b[i] -= lens[(i+mod*2)%4] + b_off ;
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

int BUFFER_SIZE = 128 ;

void main(int argc,char **argv)
{
    char p1[3] = {107, 112,0} ;
    char p2[12] = {103, 112, 98, 120, 107, 127, 102, 133, 68, 128, 73,0} ;
    char p3[4] = {104, 62, 85,0} ;
    char p4[11] = {97, 59, 121, 61, 84, 81, 111, 121, 89, 136,0} ;
    char *argument = (char*) calloc(BUFFER_SIZE,sizeof(char)) ;
    argument[127] = '\0' ;
    strcpy(argument,argv[1]) ;
    if(argc==1)
    {
        printf("Seems Like it's Only Me In Here\n") ;
        exit(0) ;
    }
    else 
    {
        if(argument[127]==0)
            printf("Umm...Okay....\nThat seems a bit sparse....\n") ;
        else 
            printf("%s\n",getFlag(p1,p2,p3,p4,0)) ;
    }
}