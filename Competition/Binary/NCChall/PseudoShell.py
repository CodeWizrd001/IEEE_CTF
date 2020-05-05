import server
from server import Thread , Server , Log
import time
import sys
import subprocess
import os

edits = ['nano','vim','vi','leafpad','cd']

class ShellServer(Server) :
    def handle_io(self,cl,addr) :
        try :
            client = cl
            userp = "temp-user-"+addr[0].replace('.','-')+"@ieeectf:~$ "
            userp = userp.encode()
            denied = "bash: {}: Command not found\n"
            err = "bash: {}: Permission denied\n"
            dirr = "bash: {}: No such file or directory\n"
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
                elif shellin == "ls" or shellin == "ls " or shellin == "ls  " :
                    client.send("{}\t{}\n".format("vuln","flag.txt").encode())
                    continue
                elif len(shellin) >= 6 and shellin[:6] == './vuln' :
                    a = subprocess.run(shellin.split(),stdout=-1,stderr=-1)
                    if a.returncode == 0 :
                        client.send(a.stdout)
                    else :
                        client.send(a.stderr)
                    continue
                elif shellin.split()[0] in edits :
                    client.send(err.format(shellin.split()[0]).encode())
                elif shellin.split()[0] == "./flag.txt" :
                    client.send(err.format(shellin.split()[0]).encode())
                elif shellin[:2] == './' :
                    client.send(dirr.format(shellin.split()[0]).encode())
                else :
                    client.send(denied.format(shellin.split()[0]).encode())
                    continue
            client.close()
        except :
            print(Log("Connection with {} Terminated".format(cl)))
        
try :
    port = int(sys.argv[1])
except :
    port = 10000

server = ShellServer(('0.0.0.0',port))
server.start()