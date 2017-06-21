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

    def test_max_number_one(self):
        """

        """

        try:
            self.prime_generator.generate_prime_numbers_to(1)
        except InvalidMaxNumberException:
            assert True is True

    # Verifies if the returned prime string matches the expected string
    def __verify_generate_prime_numbers(self, expected_list, max_number):
        returned_list = self.prime_generator.generate_prime_numbers_to(max_number)
        assert expected_list == returned_list
