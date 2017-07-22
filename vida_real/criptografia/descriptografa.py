from criptografa import *

def converteDeHex(string):
    #Coverte de Hex para caracteres
    return "".join([chr(int(string[i:i+2], 16)) for i in range(0, len(string), 2)])

def main():
    #Primeiro pegamos os dados de usuário e senha
    usuario = pegaDados("Usuário")
    senha = pegaDados("Senha Criptografada")

    #Depois obtemos a chave
    chave = GeraChave(usuario, len(senha)//2)

    #E a convertemos para hex
    senha_d = converteDeHex(senha)

    #Em seguida obtemos a senha descriptografada
    senha_d = encrypt(senha_d, chave)

    #E imprimimos os outros dados
    print("Senha Recuperada: ", senha_d)

if __name__ == '__main__':
    main()
