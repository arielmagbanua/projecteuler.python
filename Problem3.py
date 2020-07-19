import numpy

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(num):
    """(num) -> bool

    Returns true if the given number is a prime number and false if not.

    Keyword arguments:
    num -- Given number to test.
    """

    # convert to int64 type
    num64 = numpy.int64(num)

    for n in range(2, num64):
        if num % n == 0:
            return False

    return True


def largest_prime_factor(num=600851475143):
    """(num) -> num

    Returns the largest prime factor of the number.

    Keyword arguments:
    num -- Given number to test (default 600851475143)
    """

    # convert to int64 type
    num64 = numpy.int64(num)
    largest = numpy.int64(0)

    # if the number is prime itself then return it
    if is_prime(num64):
        return num64

    for n in range(2, num+1):
        if num % n == 0:
            # determine if this number is prime
            if is_prime(n):
                largest = n
        print(n)
    return largest


print(largest_prime_factor())
