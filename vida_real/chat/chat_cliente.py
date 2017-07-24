from socket import *

serverHost = ''
serverPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:
    msg = input("Você: ")
    sockobj.send(msg.encode())

    data = sockobj.recv(1024)
    print('Ele: ', data.decode())

sockobj.close()
