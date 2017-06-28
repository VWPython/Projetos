"""
No site da megasena está escrito que a chance de um jogador ganhar é de 1 em 50.063.860.
Escreva um programa usando número aleatorios para testar essa probabilidade
Sabemos que o jogo da megasena são 6 número entre 1 e 60 e nunca são repetidos

FIX: quebrado ainda
"""

import random

my_bet = [6, 13, 25, 33, 42, 50]
my_bet.sort()

megasena = list(range(1, 61))

number_of_tests = int(input("Número de testes: "))

tests_sum = 0

for test in range(number_of_tests):
    numbers_drawn = []
    count = 0

    while my_bet != numbers_drawn:
        megasena_sort = megasena.copy()
        numbers_drawn = []

        for i in range(6):
            number_drawn = random.choice(megasena_sort)
            numbers_drawn.append(number_drawn)
            megasena_sort.remove(number_drawn)

        numbers_drawn.sort()
        count += 1

    tests_sum += count

print("Resultado do teste %d: %d tentativas" % (test+1, count))

tests_sum /= number_of_tests

print("Média dos resultado:", tests_sum)
