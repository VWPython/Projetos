"""
Dados 3 números naturais, verifique se eles formam os lados de um triangulo
retangulo. A soma dos quadrados de dois lados (catetos) tem que dar o terceiro
lado (hipotenusa)

Ex:

    4^2 + 3^2 = 5^2
    3^2 + 5^2 = 4^2
    5^2 + 4^2 = 3^2
"""


def is_triangle_rectangle(side1, side2, side3):
    condition1 = (side1**2 + side2**2 == side3**2)
    condition2 = (side3**2 + side1**2 == side2**2)
    condition3 = (side2**2 + side3**2 == side1**2)

    if condition1 or condition2 or condition3:
        print("O triângulo é retangulo")
    else:
        print("O triângulo não é retangulo")


def main():
    side1 = int(input("Insira o primeiro lado: "))
    side2 = int(input("Insira o segundo lado: "))
    side3 = int(input("Insira o terceiro lado: "))

    is_triangle_rectangle(side1, side2, side3)

if __name__ == '__main__':
    main()
