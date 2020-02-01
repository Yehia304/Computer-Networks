import socket
import sys
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



with open('Requests.txt','r') as Filename:
    word = (Filename.readline())
    print(word)
    command = word.split(' ')
    print (command)
    print(command[0])
    print(command[1])
    Request = command[0] + ' ' +command [1]
    print(Request)


s.connect((socket.gethostname(), 500))
s.sendall(Request.encode())
time.sleep(1)

if command[0]=='GET':
    with open(command[1],"wb") as GETFile:
        while True:
            data = s.recv(4096)
            if not data:
                break
            GETFile.write(data)
if command[0]== 'POST':
    Permission = 'Can i upload something to the server?'
    s.sendall(Permission.encode())
    time.sleep(1)
    Agree = s.recv(4069)
    print(Agree)

    with open(command[1],"rb") as POSTFile:
        print("Uploading file ..")
        Dataupload = POSTFile.read()
        s.sendall(Dataupload)
