import time 
import socket
import threading
from threading import Thread
import base64
import random

wordlist = ["what_are_you_lookin_at","see_you_later_alligator",
    "after_a_while_crocodile",'tide_in_dirt_out',
    "good_food_good_life","imagination_at_work","have_it_your_way",
    "think_different","taste_the_feeling","the_best_a_man_can_get",
    "redbull_gives_you_wings","think_outside_the_bun","snap_crackle_pop"]

keylist = ['hello','world','newday','newlife','live','young','free',
    'what','when','where','who','why']

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
        thread = Thread(target=self.handle_io,args=(cl,addr,))
        thread.start()

    def handle_io(self,cl,addr) :
        x = list(wordlist)
        y = list(keylist)
        client = cl 
        client.settimeout(60)
        client.send('Welcome\n'.encode())
        client.send('How Fast Can You Decode \n\n'.encode())
        ch = random.choice(x)
        x.remove(ch)
        client.send(base64.b16encode(ch.encode())+'\n'.encode())
        op = client.recv(self.ReadBuffer).decode()
        if ch not in op :
            client.send("Incorrect\n".encode())
            client.close()
            return
        ch = random.choice(x)
        x.remove(ch)
        client.send(base64.b32encode(ch.encode())+'\n'.encode())
        op = client.recv(self.ReadBuffer).decode()
        if ch not in op :
            client.send("Incorrect\n".encode())
            client.close()
            return
        ch = random.choice(x)
        x.remove(ch)
        client.send(base64.b64encode(ch.encode())+'\n'.encode())
        op = client.recv(self.ReadBuffer).decode()
        if ch not in op :
            client.send("Incorrect\n".encode())
            client.close()
            return
        ch = random.choice(x)
        x.remove(ch)
        client.send(base64.b85encode(ch.encode())+'\n'.encode())
        op = client.recv(self.ReadBuffer).decode()
        if ch not in op :
            client.send("Incorrect\n".encode())
            client.close()
            return
        ch = random.choice(x)
        key = random.choice(y)
        x.remove(ch)
        client.send(base64.b16encode(ch.encode())+'\n'.encode())
        op = client.recv(self.ReadBuffer).decode()
        if ch not in op :
            client.send("Incorrect\n".encode())
            client.close()
            return


a = Server()
a.start()