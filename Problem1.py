"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

answer: 233168
"""


def sum_of_multiples(limit=1000):
    """(num) -> num

    Returns the calculated sum of all the multiples of 3 or 5 below the given number.

    Keyword arguments:
    num -- The number limit (default 1000)
    :return:
    """
    total = 0

    for c in range(limit):
        if c % 3 == 0 or c % 5 == 0:
            total += c

    return total


# answer to the problem
print(sum_of_multiples(1000))

# other examples
print(sum_of_multiples(10))
