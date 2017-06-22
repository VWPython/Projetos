"""
Calcule n!

Ex:

    5! = 5 x 4 x 3 x 2 x 1
    0! = 1
"""


def get_factorial(n):
    factorial = 1

    for fat in range(1, n+1):
        factorial *= fat

    return factorial


def main():
    n = int(input("Digite o valor de n: "))

    print("%d! é igual a %d" % (n, get_factorial(n)))

if __name__ == '__main__':
    main()
