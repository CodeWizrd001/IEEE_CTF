import time 
import socket
import threading
from threading import Thread

def Log(event) :
    return "[{}] {}".format(time.ctime(),event)

class Server :
    def __init__(self,addr=('0.0.0.0',10000)) :
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ReadBuffer = 8192
        self.addr = addr
        self.sock.bind(addr)
    def start(self) :
        self.sock.listen(50)
        print(Log("Listening At {}:{}".format(self.addr[0],self.addr[1])))
        while True :
            cl , addr = self.sock.accept()
            print(Log("Accepted connection from {}:{}".format(addr[0],addr[1])))
            self.handle_accepted(cl,addr)
    def handle_accepted(self,cl,addr) :
        """
        Currently handling "parallelism" by multithreading"""
        self.send = cl.send 
        self.recv = cl.recv
        thread = Thread(target=self.handle_io,args=(cl,addr,))
        thread.start()
    def handle_io(self,cl,addr) :
        """
        Should Be Overridden in child class
        Or Will Funcion as Echo server"""
        client = cl 
        client.send('Welcome\n'.encode())
        while True :
            client.send(">>> ".encode())
            a = client.recv(self.ReadBuffer)
            client.send(a)
            if 'exit' in a.decode() :
                client.close()
                break

class ShellServer(Server) :
    def __init__(self,addr=('0.0.0.0',10000)) :
        Server.__init__(self,addr=addr)
        self.denied = []
        self.den = "bash: {}: Command not found\n"
        self.err = "bash: {}: Permission denied\n"
        self.dirr = "bash: {}: No such file or directory\n"
    def handle_commands_preset(self,cl,addr) : 
        """
        Funcion handles greeting and preset commands

        Preset commands are 
        "exit"  - exit shell
        ""      - does nothing 
        denied  - Handles Commands listed in permission denied

        Can be overrided in child class
        If overrided handle_extended_commands should be explicitly called

        """
        try :
            client = cl
            userp = "temp-user-"+addr[0].replace('.','-')+"@ieeectf:~$ "
            self.userp = userp.encode()
            client.send("""
Custom Shell Server With Limited Functionality

New User Login from {} at {}
            \n""".format(addr[0],time.ctime()).encode())
            shellin = "" 
            while True:
                client.send(userp)
                shellin = client.recv(2048).decode().strip('\n')
                if shellin == "exit" or shellin == "exit " or shellin =="exit  " or shellin =="exit   " :
                    break
                elif shellin == "" :
                    continue
                elif shellin.split()[0] in self.denied :
                    client.send(self.err.format(shellin.split()[0]).encode())
                else :
                    handle_extended_commands(self,client,addr,shellin)
                    continue
            client.close()
        except :
            print(Log("Connection with {} Terminated".format(addr)))
    
    def handle_extended_commands(self,client,addr,shellin) :
        """
        Funcion handles extended list of custom commands

        Should be overrided in child class

        """
        client.send(self.den.format(shellin.split()[0]).encode())