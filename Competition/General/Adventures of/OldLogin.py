import asyncore
import sys
import random

C = ["This is not a flag\n",
"I'm sorry you're going to have to look at another line\n",
"Unfortunately this is also not a flag\n"]

Allowed = "55550333300510015"

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        self.recv(8096)
        self.send("""
Please Enter Login Credentials
User : xxxx         Pwd : xxxx
""".encode())
        try :
            self.send("User : ".encode())
            user = self.recv(8096).decode()
            self.send("Password : ".encode())
            pwd = self.recv(8096).decode()
            if user[0] == '$' :
                self.super = True
            user = user[1:]
            if len(user) != 4 or len(pwd) != 4 :
                self.send('User Or Password Length Incorrect\n'.encode())
                raise Exception
            try :
                user = int(user)
                pwd = int(pwd)
            except :
                self.send('[!] User or Password Is Not Integer\n'.encode())
                raise Exception
            comb = user + pwd
            user = user // 3
            pwd = pwd // 3
            user,pwd = str(user),str(pwd)
            if len(user) < 4 :
                user = '0'+user
            if len(pwd) < 4 :
                pwd  = '0'+pwd
            uAuth = '5555'+user+pwd+str(comb)
            self.send(r'Allowed Auth Level : {Allowed}\n'.encode())
            self.send(r'User Auth Level : {uAuth}\n'.encode())
            if uAuth != Allowed :
                raise Exception
            self.send('[+] Authorised Personel \n'.encode())
            self.send('[+] Flag Part        ieee_n   \n\n\n'.encode())
        except :
            self.send("[!] Authentication Failed\n".encode())
        finally :
            self.close()
        

class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        print("[+] Listening On Port : ",port)

    def handle_accepted(self,sock,addr):
        print('[+] Incoming connection from {}'.format(addr))
        handler = EchoHandler(sock)
        handler.super = False
        handler.auth = False

try :
    port = int(sys.argv[1])
except :
    port = 10000
server = EchoServer('0.0.0.0',port)
    
try :
    asyncore.loop()
except KeyboardInterrupt :
    print("")
    print("[!] Received Keyboard Interrupt")
    exit(0)
