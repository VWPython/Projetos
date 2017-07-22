import random

def strxor(a, b):
    """
    Realiza a operação xor para toda a string a e b
    sabendo qual das duas é maior
    """
    # xor em duas strings de tamanhos diferentes
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encrypt(chave, msg):
    """
    Encripta uma mensagem usando o método do One Time Pad
    """
    #Para criptografar a mensagem nós fazemos uma operação
    #xor para cada 8 bits (1 char) da mensagem
    c = strxor(chave, msg)
    return c

def converteParaHex(string):
    #Converte de caracteres para hex
    c = ""
    for l in string:
        h = hex(ord(l))
        h = h[2:len(h)]
        if len(h) < 2:
            h = "0" + h
        c += h
    return c

def pegaDados(tipo):
    """
    Pega os dados do usuário, sendo tipo
    'usuário' ou 'senha'
    """
    while True:
        d = input("Digite %s\n"%tipo)
        ok = True
        for c in d:
            if not 0 < ord(c) < 256:
                print("Caracter não aceito")
                ok = False
                break
        if ok:
            return d

def ObtemSeed(usuario):
    """
    Este trecho obterá o inteiro a partir
    do nome do usuário para usar como seed do
    gerador
    """
    soma = 0
    for c in usuario:
        soma += ord(c)

    random.seed(soma)

def GeraChave(usuario, tamanho):
    """
    Iremos gerar a chave para criptografar a senha a partir
    do nome do usuário
    """
    ObtemSeed(usuario)
    chave = ""

    for i in range(tamanho):
        chave += chr(random.randint(0, 256))

    #Um detalhe sobre a forma como foi feita é que
    #não obteremos uma chave única, dependendo da
    #nome de usuário, poderemos ter somas iguais
    #para usuários diferentes, o que possibilitaria
    #chaves iguais. O ideial seria representar cada
    #usuário com um número inteiro único e usar esse
    #número inteiro para criptografar. Como não temos
    #vários usuários, utilizaremos esse método totalmente
    #falho
    return chave


def main():
    """
    Função principal do programa
    """
    #Primeiro pegamos os dados de usuário e senha
    usuario = pegaDados("Usuário")
    senha = pegaDados("Senha")

    #Depois obtemos a chave
    chave = GeraChave(usuario, len(senha))

    #Em seguida obtemos a senha criptografada
    senha_c = encrypt(chave, senha)

    #E a convertemos para hex
    senha_c = converteParaHex(senha_c)

    #E imprimimos os outros dados
    print("Senha Criptografada: ", senha_c)


if __name__ == '__main__':
    main()
