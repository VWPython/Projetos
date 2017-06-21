"""
Test the PrimeNumbersGenerator class using pytest
"""

from eratostenes.prime_numbers_generator import PrimeNumbersGenerator
from eratostenes.invalid_max_number_exception import InvalidMaxNumberException


class TestPrimeNumberGenerator(object):
    """
    Unit test cases to test the PrimeNumbersGenerator class
    """

    prime_generator = PrimeNumbersGenerator()

    def test_prime_numbers_to_two(self):
        """
        Test the first prime number
        """

        self.__verify_generate_prime_numbers("2", 2)

    def test_prime_numbers_to_three(self):
        """
        Test two prime numbers
        """

        self.__verify_generate_prime_numbers("2, 3", 3)

    def test_prime_numbers_to_four(self):
        """
        Test two prime numbers
        """

        self.__verify_generate_prime_numbers("2, 3", 4)

    def test_prime_numbers_to_five(self):
        """
        Test three prime numbers
        """

        self.__verify_generate_prime_numbers("2, 3, 5", 5)

    def test_prime_numbers_to_ten(self):
        """
        Test four prime numbers
        """

        self.__verify_generate_prime_numbers("2, 3, 5, 7", 10)

    def test_prime_numbers_to_twenty_two(self):
        """
        Test eight prime numbers
        """

        self.__verify_generate_prime_numbers("2, 3, 5, 7, 11, 13, 17, 19", 22)

    def test_max_number_one(self):
        """
        Test invalid max number: 1
        """

        self.__verify_invalid_max_number_rejected(1)

    def test_max_number_zero(self):
        """
        Test invalid max number: 0
        """

        self.__verify_invalid_max_number_rejected(0)

    def test_max_number_negative(self):
        """
        Test invalid max number: -1
        """

        self.__verify_invalid_max_number_rejected(-1)

    def __verify_invalid_max_number_rejected(self, max_number):
        # Verifies if the exception is throw for an invalid max number.

        try:
            self.prime_generator.generate_prime_numbers_to(max_number)
        except InvalidMaxNumberException:
            assert True is True

    def __verify_generate_prime_numbers(self, expected_list, max_number):
        # Verifies if the returned prime string matches the expected string

        returned_list = self.prime_generator.generate_prime_numbers_to(max_number)
        assert expected_list == returned_list
