"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ans: 232792560
"""


def gcd(numerator, denominator):
    """(num, num) -> num
    Calculates the GCD (greatest common denominator) recursively.

    Keyword arguments:
    numerator -- The numerator
    denominator -- The denominator
    """

    if denominator == 0:
        return numerator
    return gcd(denominator, numerator % denominator)


def smallest_number(limit):
    """(num) -> num

    Get the smallest number that can be divided from 1 to limit without any remainder.

    Keyword arguments:
    limit -- The number limit
    """

    lcm = 1

    for i in range(1, limit+1):
        lcm = (lcm * i) / gcd(lcm, i)

    return int(lcm)


print(smallest_number(20))
