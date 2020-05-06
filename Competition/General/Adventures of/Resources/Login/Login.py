import sys
import socket
import threading
from threading import Thread
import os
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Socket Configuration

ip = '0.0.0.0'
try :
    port = int(sys.argv[1])
except :
    port = 10000

sock.bind((ip,port))
sock.listen(50)                                                  # Socket Listening

rBuff = 8192

onlineList = {}

story = """
He enters the password and the surface beneath him starts to crumble .
He keeps falling and falling and everything goes dark .

As he regained his consiousness all he could here was a repeating chant.
"HURAKEN WILL LEAD YOU THROUGH THE MAZE[1] , HURAKEN WILL LEAD YOU THROUGH THE MAZE
HURAKEN WILL LEAD YOU THROUGH THE MAZE" .His vision cleared and he saw a large 
creature fly .It was a Dragon disappearing into the distance still roaring 
"HURAKEN WILL LEAD YOU THROUGH THE MAZE".Who is Huraken ? and what Maze ?
So many questions and yet one question shadowed all the others . How did he just 
see a dragon ? He must definitely be dreaming .Mind still wandering he felt a tap
on his shoulder.He looked up and saw a young man with a brawny build yet bruises 
all over.But the bruises did'nt seem to bother the guy ."Name's Azriel.Who are you ?"
he asked .And Gamer answered with his alias "UltGamer but call me Gamer" .
"Okay Gamer what brings you to these parts ?"."Where am I ?What is this place?"
asked the befuddled Techie ."This is nowhere. And YOU should'nt be here." 

Password to the zipfile zip_q.zip is    hippie
Password to the zipfile zip_p.zip is    hello

""".encode()

if not os.path.exists("Login_Log") :                            # Logging Setup
    os.mkdir("Login_Log")
ELog = open("Login_Log\\ErrorsLog.txt",mode="w")
ALog = open("Login_Log\\AccessLog.txt",mode="w")
SLog = open("Login_Log\\ServerLog.txt",mode="w")
def Log(event) :
    return "[{}] {}\n".format(time.ctime(),event)

Allowed = "55550333300510015"
class AuthException(Exception) :
    pass

SLog.write(Log("Listening On {}:{}".format(ip,port)))

class User :
    def __init__(self,addr) :
        self.addr = addr

def recv(client) :
    return client.recv(rBuff).decode().strip("\n")

def handle(client,addr) :
    user = User(addr)
    try :
        client.send("""
Entered Secure System

Defender G Secure Terminal
        
Please Enter Login Credentials
User : xxxx         Pwd : xxxx
""".encode())
        client.send("User : ".encode())
        user.name = recv(client)
        client.send("Password : ".encode())
        user.pas = recv(client)
        user.super = False
        if '$' in user.name :
            temp = list(user.name)
            temp.remove('$')
            user.name = ''.join(temp)
            user.super = True
        if len(user.name) != 4 or len(user.pas) != 4 :
            client.send("[!] Length Of User or Password Incorrect\n".encode())
            raise AuthException
        try :
            user.u = int(user.name)
            user.p = int(user.pas)
        except ValueError :
            client.send("[!] User or Password Not Integer\n".encode())
            raise AuthException
        comb = user.u + user.p
        u = user.u // 3 
        p = user.p // 3
        u,p = str(u),str(p)
        if len(u) < 4 :
            u = '0'+u
        if len(p) < 4 :
            p = '0'+p
        uAuth = '5555'+u+p+str(comb)
        client.send('Allowed Auth Level : {}\n'.format(Allowed).encode())
        client.send('User Auth Level : {}\n'.format(uAuth).encode())
        if uAuth != Allowed :
            raise AuthException
        client.send('[+] Authorised Personel \n'.encode())
        client.send('[+] Flag Part 1 out of 9        Z3u5_Ult      \n\n\n'.encode())
        client.send("[+] The password to zip file zip_q.zip is      hippie     \n\n".encode())
        if not user.super :
            client.send(story)
        if user.super :
            for i in range(5) :
                client.send('.\n'.encode())
                time.sleep(0.1)
            client.send('[+] Super User Level Detected')
            client.send('[+] Flag Part 9 out of 9        ----xxxX      \n\n\n'.encode())
        client.close()
    except ConnectionAbortedError :
        ELog.write(Log("Client {} Terminated Unexpectedly".format(addr)))
    except AuthException :
        client.send("[-] Auth Failed \n".encode())
        client.close()
    except Exception as e :
        ELog.write(Log(e))
        client.close()
    finally :
        client.close()
    SLog.write(Log("Terminating Thread {}".format(addr)))
    # onlineList.pop(client)

print("[+] Starting")
try :
    while True :
        c , addr = sock.accept()
        ALog.write(Log("Accepted Connection From {}".format(addr)))
        SLog.write(Log("Starting Thread for {}".format(addr)))
        thread = Thread(target=handle,args=(c,addr,))
        # onlineList[c] = thread
        thread.start()
except KeyboardInterrupt :
    SLog.write(Log("KeyboardInterrupt"))
    SLog.write(Log("Quitting"))
    print("[!] Exited")
    SLog.close()
    ELog.close()
    ALog.close()
    exit(0)
