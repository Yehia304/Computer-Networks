import socket
import sys
import time
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % err)

s.bind((socket.gethostname(), 500))
s.listen(5)
print("socket is listening")

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connected to {address} ")
    data=clientsocket.recv(4096)
    print(data)
    data1= data.decode()
    print(data1)
    Request = data1.split(' ')
    print(Request[0])
    print(Request[1])

    if Request[0]=='GET':
        print('GET SUCCESSFULLY DETECTED')
        Filename = Request[1].strip()
        print("File name" + Filename)
        with open(Filename, "rb") as GETFile:
            #send file
            print("Sending file...")
            data = GETFile.read()
            clientsocket.sendall(data)

    if Request[0] == 'POST':
        print('POST SUCCESSFULLY DETECTED')
        Filename = Request[1].strip()
        print("File name" + Filename)
        Permission = clientsocket.recv(4096)
        print(Permission)
        Agree = "200 \OK"
        clientsocket.sendall(Agree.encode())
        time.sleep(1)
        with open(Filename,"wb") as POSTFile:
            while True:
                Datauploaded = clientsocket.recv(4096)
                if not Datauploaded:
                    break

                POSTFile.write(Datauploaded)

    sys.exit(0)


