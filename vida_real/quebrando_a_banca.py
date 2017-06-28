"""
Escreve um programa que teste se a estatistica proposta no filme
'Quebrando a banca' é verdadeira, que diz que ao ter 3 escolhas temos 33,3% de
chance de acerta e ao eliminar uma escolha, ficamos com 66,6% logo é viavel
fazer a troca da escolha feita anteriormente para a nova opção que
disponibilizaram.

User quantidades de testes significativas por exemplo: 100000
"""

from random import randint


def main():
    tests = int(input("Digite o numero de testes a realizar: "))

    change = 0
    not_change = 0

    for i in range(tests):
        door = randint(1, 3)
        premium = randint(1, 3)

        if door == premium:
            not_change += 1
        else:
            change += 1

    print("É vantajoso trocar em %3g%% das vezes" % (change*100/tests))
    print("Não é vantajoso trocar em %3g%% das vezes" % (not_change*100/tests))

if __name__ == '__main__':
    main()
