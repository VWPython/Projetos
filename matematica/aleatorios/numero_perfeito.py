import doctest


def perfect_number(input_number):
    """
    Return if the number is a perfect number

    A perfect number is an integer for which the sum of all its positive
    divisors (excluding the number itself) is equal to it.

    Parameters:

        @param number: Number that will be verify
        @type number: integer

    Return:

        True if the number is perfect and False if not

    Example:

        >>> perfect_number(0)
        Traceback (most recent call last):
        ...
        ValueError: Number has to be bigger than zero!

        >>> perfect_number(-1)
        Traceback (most recent call last):
        ...
        ValueError: Number has to be bigger than zero!

        >>> perfect_number(27)
        False

        >>> perfect_number(28)
        True

        >>> perfect_number(6)
        True

        >>> perfect_number(496)
        True

        >>> perfect_number(8128)
        True
    """

    sum = 0

    if input_number < 1:
        raise ValueError("Number has to be bigger than zero!")

    for number in range(input_number):
        number += 1
        if input_number % (number) == 0 and \
           (number) != input_number:

            sum += number

    if sum == input_number:
        return True
    else:
        return False


def main():
    input_number = int(input("Insira um número inteiro maior que zero: "))

    print(perfect_number(input_number))


if __name__ == '__main__':
    main()
