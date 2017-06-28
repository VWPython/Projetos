"""
Main file to execute Eratostenes algorithm
"""
from eratostenes.prime_numbers_generator import PrimeNumbersGenerator


def main():
    """
    Client funcionality
    """

    generator = PrimeNumbersGenerator()

    max_number = int(input("Insert the prime max number: "))

    print(generator.generate_prime_numbers_to(max_number))

if __name__ == '__main__':
    main()
