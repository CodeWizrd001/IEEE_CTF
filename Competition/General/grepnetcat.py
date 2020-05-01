import asyncore
import sys
import random

C = ["This is not a flag\n",
"I'm sorry you're going to have to look at another line\n",
"Unfortunately this is also not a flag\n"]

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        self.i += 1
        self.send(random.choice(C).encode()) 
        if self.i == 2500 :
            self.send("ieee_nitc{Y0uR3_W3LcoMe}\n".encode())
        if self.i == 5000 :
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
        handler.i = 0

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
