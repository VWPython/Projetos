"""
Faça um programa para um caixa eletronico, o programa deve perguntar ao usuário
o valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponiveis serão 1, 2, 5, 10, 20, 50 e 100 reais.

Ex:

    cash = 1469

    14 notas de R$ 100,00
    1 nota de R$ 50,00
    1 nota de R$ 10,00
    1 nota de R$ 5,00
    2 notas de R$ 2,00
"""


def get_hundred_notes(cash):
    """
    Takes the number of one hundred dollar cedulas of the inserted value
    """

    hundred_notes = cash // 100
    cash = cash % 100

    if hundred_notes > 0:
        if hundred_notes > 1:
            print(hundred_notes, "notas de R$ 100,00")
        else:
            print(hundred_notes, "nota de R$ 100,00")

    return cash


def get_fifty_notes(cash):
    """
    Take the number of fifty-dollar cedulas of the inserted value
    """

    fifty_notes = cash // 50
    cash = cash % 50

    if fifty_notes > 0:
        if fifty_notes > 1:
            print(fifty_notes, "notas de R$ 50,00")
        else:
            print(fifty_notes, "nota de R$ 50,00")

    return cash


def get_twenty_notes(cash):
    """
    Take the number of twenty-dollar cedulas of the inserted value
    """

    twenty_notes = cash // 20
    cash = cash % 20

    if twenty_notes > 0:
        if twenty_notes > 1:
            print(twenty_notes, "notas de R$ 20,00")
        else:
            print(twenty_notes, "nota de R$ 20,00")

    return cash


def get_ten_notes(cash):
    """
    Take the number of ten-dollar cedulas of the inserted value
    """

    ten_notes = cash // 10
    cash = cash % 10

    if ten_notes > 0:
        if ten_notes > 1:
            print(ten_notes, "notas de R$ 10,00")
        else:
            print(ten_notes, "nota de R$ 10,00")

    return cash


def get_five_notes(cash):
    """
    Take the number of five-dollar cedulas of the inserted value
    """

    five_notes = cash // 5
    cash = cash % 5

    if five_notes > 0:
        if five_notes > 1:
            print(five_notes, "notas de R$ 5,00")
        else:
            print(five_notes, "nota de R$ 5,00")

    return cash


def get_two_notes(cash):
    """
    Take the number of two-dollar cedulas of the inserted value
    """

    two_notes = cash // 2
    cash = cash % 2

    if two_notes > 0:
        if two_notes > 1:
            print(two_notes, "notas de R$ 2,00")
        else:
            print(two_notes, "nota de R$ 2,00")

    return cash


def get_one_coin(cash):
    """
    Take the number of one-dollar coin of the inserted value
    """

    one_coin = cash // 1
    cash = cash % 1

    if one_coin > 0:
        if one_coin > 1:
            print(one_coin, "moedas de R$ 1,00")
        else:
            print(one_coin, "moeda de R$ 1,00")

    return cash


def print_cash(cash):
    """
    Print the number of money cedulas
    """

    cash = get_hundred_notes(cash)
    cash = get_fifty_notes(cash)
    cash = get_twenty_notes(cash)
    cash = get_ten_notes(cash)
    cash = get_five_notes(cash)
    cash = get_two_notes(cash)
    get_one_coin(cash)


def main():
    cash = int(input("Digite o valor do saque: "))
    print_cash(cash)

if __name__ == '__main__':
    main()
