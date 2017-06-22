"""
Dado um inteiro positivo n, calcule e imprima o valor da seguinte soma:
    S = 1/n + 2/(n-1) + 3/(n-2) + ... + n/1
"""

n = int(input("Digite o valor de n: "))

S = 0.0

for i in range(1, n+1):
    S += i/(n - i + 1)

print("A soma é:", S)
