from eratostenes.validations_exception import InvalidInsertedNumberException


class PrimeNumbersCalculator(object):
    """
    Prime numbers generator using Eratostenes algorithm.
    Take a number and marks its multiples.
    The remaining numbers are prime numbers.

    Example:

        2 to 22 is True
        2*2 to 22 = 4(False), 6(False), 8(False), 10(False), 12(False), ...
        2*3 to 22 = 6(False), 9(False), 12(False), ...
        2*5 to 22 = 10(False), 15(False), 20(False)
    """

    inserted_number = 0
    SMALLEST_PRIME = 2

    def __init__(self, inserted_number):
        self.inserted_number = inserted_number
        self.prime_list = self.__initializes_prime_list()

    def calculate(self):
        # get the list of prime numbers or an invalidMaxNumber exception

        if (self.inserted_number >= self.SMALLEST_PRIME):
            return self.__get_prime_numbers()
        else:
            raise InvalidInsertedNumberException()

    def __get_prime_numbers(self):
        # Generates prime numbers to n using Eratostenes algorithm.

        potential_prime_numbers = range(self.SMALLEST_PRIME, self.inserted_number + 1)

        for number in potential_prime_numbers:
            self.__verify_if_is_prime(number)

        return self.__format_string_result()

    def __verify_if_is_prime(self, number):
        # Verify if the potential prime number is prime

        is_prime = self.prime_list[number]

        if (is_prime):
            self.__insert_false_on_multiples_prime(number)

    def __insert_false_on_multiples_prime(self, number):
        # When get the prime number insert false on their multiple

        multiple_number = self.SMALLEST_PRIME * number
        increment_number = number
        multiple_numbers = range(multiple_number, self.inserted_number + 1, increment_number)

        for number in multiple_numbers:
            self.prime_list[number] = False

    def __format_string_result(self):
        # Insert all prime numbers until inserted number on string result with format "2, 3, 5, ..."

        COMMA = ', '
        string_result = str(self.SMALLEST_PRIME)
        prime_numbers = range(self.SMALLEST_PRIME + 1, self.inserted_number + 1)

        for number in prime_numbers:
            is_prime = self.prime_list[number]

            if (is_prime):
                string_result += COMMA + str(number)

        return string_result

    def __initializes_prime_list(self):
        # Initializes the array with True on all potential prime numbers that going from 2 until inserted number

        potential_prime_list = []

        potential_prime_list.append(False)
        potential_prime_list.append(False)

        number = int(self.SMALLEST_PRIME)

        while (number <= self.inserted_number):
            potential_prime_list.append(True)
            number += 1

        return potential_prime_list
