import server
import random
import sys
from server import Server ,ShellServer

flag = "ieee_nitc{WelL_N0W_You_Kn0W_wHo_Y0u_aR3}\n".encode()

accepted = ['whoami','who','w']

class MyServer(ShellServer) :
    def handle_extended_commands(self,client,addr,comm) :
        cList = comm.split()
        if cList[0] in accepted and self.flagAccess :
            self.send(self.userp)
            self.send('\n'.encode())
            self.send(flag)
            self.send('\n'.encode())
            self.close()
        elif cList[0] == 'help' :
            self.send(b'There seems to be a serious problem here\nYou have to get to the root of \nthe issue\n')
        elif cList[0] == 'cd' :
            if len(cList)==1 or cList[1] == '~' or cList[1] == '~/' :
                self.curDir = []
            elif cList[1] == '..' :
                self.curDir.pop()
            else :
                self.send(b'bash : cd : Operation not supported\n')
            if self.curDir == [] :
                self.flagAccess = True
                self.send(b'Okay now you\'re in the root\n')
                self.send(b'Now all you\'ve gotta do is make \nthe terminal print your shell username\n')
        else :
            self.send(self.den.format(comm.split()[0]).encode())

try :
    port = int(sys.argv[1])
except :
    port = 10000

try :
    server = MyServer(('0.0.0.0',port))
    server.denied = ['echo','print','id','su','sudo']
    server.flagAccess = False
    server.curDir = ['CTF','Challenges','tempUser'+str(random.randint(100,999))]
    server.start()
except :
    print(Log("KeyBoardInterrupt"))
    exit(0)