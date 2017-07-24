from socket import *

meuHost = ''
minhaPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(1)


while True:
    conexão, endereço = sockobj.accept()
    print('Server conectado por', endereço)
    
    while True:
        data = conexão.recv(1024)
        print("Ele: ", data.decode())
        
        resposta = input("Você: ")

        conexão.send(resposta.encode())

    conexão.close()
