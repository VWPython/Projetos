from eratostenes.prime_numbers_calculator import PrimeNumbersCalculator


class PrimeNumbersGenerator(object):
    """
    Prime numbers generator using Eratostenes algorithm.
    """

    def generate_prime_numbers_to(self, number_inserted):
        """
        Generates prime numbers to 'n' using Eratostenes algorithm.

        Parameters:

            @param number_inserted: Generate prime numbers from 2 to inserted number
            @type max_number: Integer

        Return:

            @return: String with generated prime numbers.
            @rtype: String

        Exception:

            @raise: Invalid max number exception if the max number is less than 2

        Example:

            max_number = 7

            return: "2, 3, 5, 7"
        """

        prime_numbers_calculator = PrimeNumbersCalculator(number_inserted)
        return prime_numbers_calculator.calculate()
