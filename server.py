import socket
from _thread import *
import sys


server="172.26.224.1"
port=5555
arr=[(0,0),(100,100)]
usernumber=0


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)



s.listen(2)
print("server started")

def convertttos(tuple):
    return (str(tuple[0])+','+str(tuple[1]))


def convertstot(string):
    list=string.split(',')
    # for l in list:
    return (int(list[0]),int(list[1]))

def threaded_client(conn,num):
    global usernumber
    conn.send(str.encode(convertttos(arr[num])))
    reply=""
    while True:
        try:
            # amount of bites we are abole to reciveve from the client
            data=convertstot(conn.recv(2048).decode())
            # reply=data.decode("utf-8")
            arr[num]=data
            if not data:
                print("disconnected")
                break
            else:
                if num==1:
                    reply=arr[0]
                else:
                    reply=arr[1]
            conn.sendall(str.encode(convertttos(reply)))
        except:
            break
    print("lost connectin")
    usernumber-=1
    if num==1:
         arr[1]=(100,100)
    else:
        arr[0]=(0,0)
    conn.close()
    pass


while True:
    (conn,addr)=s.accept()
    print(f"connected to {addr}")

    start_new_thread(threaded_client,(conn,usernumber))
    usernumber+=1

