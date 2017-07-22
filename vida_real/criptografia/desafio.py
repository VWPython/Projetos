"""
Nós criamos um novo website e queremos salvar os 
nomes de usuário e senha em nosso database

Entretanto por motivos de segurança nós temos que
criptografar o a senha de todos os usuários

Para isso vamos criar um algoritmo de criptografia
tosco, que tal?

Para tanto vamos usar um método de criptografia chamado
One Time Pad

O One Time Pad funciona da seguinte forma:
Temos uma dada mensagem, por exemplo
	Ola Mundo
E queremos criptografa-la.
Para tanto iremos pegar uma chave que possua
o mesmo tamanho da string 'Ola Mundo', isto é
uma chave de 9 caracteres

Então faremos o seguinte: Cada caracter tem um número
inteiro representativo. Vamos supor, como facilitação,
que as senhas do usuário só contenham caracteres da tabela
ASCII e portanto todo caracter colocado na senha pode ser
representado como um número binário de 8 bits

Pegaremos o número inteiro do carácter e o tomaremos
o seu número binário, a partir dele utilizaremos a chave
e faremos para cada binário uma operação de Bitwise XOR
para um novo número binário.

Em seguida para cada binário obtido colocaremos ele na
representação hexadecimal e colocaremos numa única string
a soma de todos os números hexadecimais obtidos

Um método importante para esse propósito é o encode de strings
veja na documentação do python sobre ele.

Entretanto a grande sacada do método One Time Pad é que a chave
é única para cada vez que uma mensagem é criptografada.
Ou seja, é preciso obter uma string aleátoria como chave para
cada vez que quisermos criptografar uma mensagem, podemos fazer
isso utilizando o módulo random e sua função seed.

A função seed, que recebe um inteiro, fará com que, para aquele
dado inteiro, teremos uma sequência de 'sorteios' bem definido,
por exemplo, execute o seguinte código

import random

random.seed(1234)
print(random.random())

Diversas vezes e verá que a saída é sempre a mesma

Tente a partir desse método criar um sistema de criptografia
para seu website.

OBS: JAMAIS USE ESSE MÉTODO PARA UM WEBSITE REAL, O GERADOR
NÃO É ADEQUADO NEM A FORMA COMO FOI EXECUTADO A GERAÇÃO DA
CHAVE
"""
