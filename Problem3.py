import math

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

ans: 6857
"""


def largest_prime_factor(num=600851475143):
    """(num) -> num

    Returns the largest prime factor of the number.

    Keyword arguments:
    num -- Given number to test (default 600851475143)
    """

    # initialize the largest prime
    largest_prime = -1

    # the number of 2s that divide num
    while num % 2 == 0:
        largest_prime = 2
        num >>= 1  # equivalent to n /= 2

    # num must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            largest_prime = i
            num = num / i

    # This condition is to handle the
    # case when num is a prime number
    # greater than 2
    if num > 2:
        largest_prime = num

    return int(largest_prime)


print(largest_prime_factor(13195))
print(largest_prime_factor())
