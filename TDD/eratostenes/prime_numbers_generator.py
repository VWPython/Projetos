from eratostenes.invalid_max_number_exception import InvalidMaxNumberException


class PrimeNumbersGenerator(object):
    """
    Prime numbers generator using Eratostenes algorithm.
    Take a number and marks its multiples.
    The remaining numbers are prime numbers.
    """

    SMALLEST_PRIME = 2

    def generate_prime_numbers_to(self, max_number):
        """
        Generates prime numbers to 'n' using Eratostenes algorithm.

        @Param max_number: Generate prime numbers from 2 to max_number.

        @Return: String with generated prime numbers.

        @Example:

            max_number = 7

            return: "2, 3, 5, 7"
        """

        if (max_number >= self.SMALLEST_PRIME):
            return self.__get_prime_numbers(max_number)
        else:
            raise InvalidMaxNumberException()

    def __get_prime_numbers(self, max_number):
        # Generates prime numbers to n using Eratostenes algorithm.

        is_prime = self.__initializes_potential_prime_list(max_number)

        # Insert False on not prime numbers
        # Ex: 2 -> 22 is True
        # 2*2 -> 22 = 4(False), 6(False), 8(False), 10(False), 12(False), ...
        # 2*3 -> 22 = 6(False), 9(False), 12(False), ...
        # 2*5 -> 22 = 10(False), 15(False), 20(False)
        for value in range(self.SMALLEST_PRIME, max_number + 1):
            if (is_prime[value]):
                for not_prime in range(self.SMALLEST_PRIME * value, max_number + 1, value):
                    is_prime[not_prime] = False

        return self.__format_result(max_number, is_prime)

    def __format_result(self, max_number, is_prime):
        # Create the result string with all prime numbers from smallest prime
        # until max number

        result = str(self.SMALLEST_PRIME)

        # Insert all prime numbers until max number on string result
        # on format "2, 3, 5, ..."
        for number in range(self.SMALLEST_PRIME + 1, max_number +1):
            if (is_prime[number]):
                result += ", " + str(number)

        return result

    def __initializes_potential_prime_list(self, max_number):
        # Initializes the array with all the numbers from 0 to max_number

        potential_prime_list = []

        potential_prime_list.append(False)
        potential_prime_list.append(False)

        # Insert True on all potential prime numbers that going from 2 until max
        # number
        number = int(self.SMALLEST_PRIME)
        while (number < max_number + 1):
            potential_prime_list.append(True)
            number += 1

        return potential_prime_list
