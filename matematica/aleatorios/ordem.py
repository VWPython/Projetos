"""
Faça um programa que leia três números e mostre-os em ordem decrescente e
crescente
"""


def descending_order(n1, n2, n3):
    """
    Sort numbers in descending order
    """

    if n1 >= n2 >= n3:
        print(n1, n2, n3)
    elif n1 >= n3 >= n2:
        print(n1, n3, n2)
    elif n2 >= n1 >= n3:
        print(n2, n1, n3)
    elif n2 >= n3 >= n1:
        print(n2, n3, n1)
    elif n3 >= n1 >= n2:
        print(n3, n1, n2)
    else:
        print(n3, n2, n1)


def ascending_order(n1, n2, n3):
    """
    Sort numbers in ascending order
    """

    if n1 >= n2 >= n3:
        print(n3, n2, n1)
    elif n1 >= n3 >= n2:
        print(n2, n3, n1)
    elif n2 >= n1 >= n3:
        print(n3, n1, n2)
    elif n2 >= n3 >= n1:
        print(n1, n3, n2)
    elif n3 >= n1 >= n2:
        print(n2, n1, n3)
    else:
        print(n1, n2, n3)

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    descending_order(n1, n2, n3)
    ascending_order(n1, n2, n3)

if __name__ == '__main__':
    main()
