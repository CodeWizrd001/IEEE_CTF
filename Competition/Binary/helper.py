import random
import sys

def encodeGenerator(string,mod) :
    l = len(string)
    al = random.randint(1,l-6)
    print(al,end=" ")
    bl = random.randint(1,l-al-4)
    print(bl,end=" ")
    cl = random.randint(1,l-al-bl-2)
    print(cl,end=" ")
    dl = l-al-bl-cl
    print(dl)
    n = al+bl+cl+dl 
    lens = [al,bl,cl,dl]
    print(l,n)
    p1 = list(map(ord,string[:al]))
    p2 = list(map(ord,string[al:al+bl]))
    p3 = list(map(ord,string[al+bl:al+bl+cl]))
    p4 = list(map(ord,string[n-dl:n]))
    b_off = (mod*5)%3 ;
    c_off = (mod*7)%3 ;
    d_off = (mod*8)%3 ; 
    print("Encoded : ") 
    for i in range(len(p1)) :
        p1[i] += lens[i%4]
    for i in range(len(p2)) :
        p2[i] += lens[(i+mod*5)%4] + b_off
    for i in range(len(p3)) :
        p3[i] += lens[(i+mod*3)%4] + c_off
    for i in range(len(p4)) :
        p4[i] += lens[(i+mod*5)%4] + d_off
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(lens)

def decodeGenerated(mod) :
    p1 = a = [114, 107, 103, 113, 104, 116, 107, 128, 108]
    p2 = b = [132, 108, 110, 109, 112, 101]
    p3 = c = [125, 117]
    p4 = d = [104, 104, 103, 107, 110, 116, 101, 123, 109, 107, 102, 137]
    lens = list(map(len,[a,b,c,d]))
    al , bl , cl , dl = lens
    b_off = (mod*5)%3 ;
    c_off = (mod*7)%3 ;
    d_off = (mod*8)%3 ; 
    print("Encoded : ") 
    print(a,b,c,d,sep="\n")
    for i in range(len(p1)) :
        p1[i] -= lens[i%4]
    for i in range(len(p2)) :
        p2[i] -= lens[(i+mod*2)%4] + b_off
    for i in range(len(p3)) :
        p3[i] -= lens[(i+mod*3)%4] + c_off
    for i in range(len(p4)) :
        p4[i] -= lens[(i+mod*5)%4] + d_off
    p1 = ''.join(list(map(chr,p1)))
    p2 = ''.join(list(map(chr,p2)))
    p3 = ''.join(list(map(chr,p3)))
    p4 = ''.join(list(map(chr,p4)))
    print(p1,p2,p3,p4,sep="")

if __name__ == "__main__" :
    try :
        flag = sys.argv[1]
        mod = int(sys.argv[2])
        encodeGenerator(flag,mod)
    except :
        decodeGenerated(0)