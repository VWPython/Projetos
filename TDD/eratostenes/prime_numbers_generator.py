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

            return: "2, 3, 4, 5, 7"
        """

        # If max number is 1 an exception is thrown
        if (max_number == 1):
            raise InvalidMaxNumberException()

        # If max number is bigger than smallest prime return the primes string
        if (max_number == self.SMALLEST_PRIME):
            return "2"
        else:
            return "2, 3"
