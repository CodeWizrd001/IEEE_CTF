import server
from server import Server , ServerFarm ,Log
from threading import Thread
import random

_ = [' ']
p = ['p','P']
a = ['a','A','4']
r = ['r','R']
t = ['t','T']
o = ['o','O','0']
f = ['f','F']
l = ['l','L']
g = ['g','G','6']
u = ['u','U']
_1 = ['1']

def getId() :
    id = list(map(random.choice,[_,_,_,p,a,r,t,_,o,f,_,f,l,a,g,_,o,u,t,_,o,f,_,_1,_1,_]))
    return ''.join(id)

flag = ['iee', 'e_n', 'itc', '{SH', '4RK', 'b0Y', '_4n', 'd_l', 'aVA', '61r', 'L}']

allowed = ['drip','dust','loud','flight','damaging','homely']

def flagF(chunk) :
    f = "\n\n\n"+getId()+"\n"+chunk+"\n\n\n\n\n\n   "
    f = f.encode()
    return f

class FlagServer(Server) :
    def __init__(self,addr=('0.0.0.0',8000)) :
        Server.__init__(self,addr=addr)
    def handle_io(self,cl,addr) :
        i = 0
        client = cl 
        client.send('Welcome\n'.encode())
        while True :
            i += 1
            try :
                client.send(">>> ".encode())
                a = client.recv(self.ReadBuffer)
                client.send(a)
                if a.decode().split('\n')[0] in allowed and flag != [] :
                    # print(Log("Flag Send {} to {}".format(self.addr,addr)))
                    fl = flagF(flag.pop(random.randint(0,len(flag)-1)))
                    print(fl.decode())
                    client.send(fl)
                    print(Log("Flag Sent {} to {}".format(self.addr,addr)))
                if 'exit' in a.decode() :
                    client.close()
                    break
            except OSError :
                print(Log("OSError {}".format(addr)))
                client.close()
                break
            except BaseException as e :
                print(Log("{} cause by {}".format(e,addr)))
                break
            finally :
                print(Log("Connection with {} terminated".format(addr)))

def FlagFun(port) :
    a = FlagServer(addr=('0.0.0.0',port))
    a.start()

if __name__ == "__main__" :
    for i in range(8000,8100) :
        th = Thread(target=FlagFun,args=(i,))
        th.start()