#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *decodeFlag(char *a,char *b,char *c,char *d,int mod)
{
    int la,lb,lc,ld ;
    la = strlen(a) ;
    lb = strlen(b) ;
    lc = strlen(c) ;
    ld = strlen(d) ;
    int lens[4] = {la,lb,lc,ld} ;
    int n = la+lb+lc+ld ;
    int i = 0;
    char *eFlag = (char*) calloc(la+lb+lc+ld+1,sizeof(char)) ;
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

void main(int argc,char **argv)
{
    char p1[11] = {115, 114, 102, 106, 105, 123, 106, 121, 109, 136,0} ;
    char p2[14] = {112, 121, 98, 108, 105, 129, 112, 100, 108, 114, 96, 106, 120,0} ;
    char p3[2] = {109,0} ;
    char p4[6] = {121, 113, 102, 105, 135,0} ;
    printf("%s\n",decodeFlag(p1,p2,p3,p4,0)) ;
}