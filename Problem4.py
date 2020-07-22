"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ans: 906609
"""


def largest_number_palindrome():
    """
    todo: Needs improvement
    Return the largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome = 0

    for c in range(100, 1000):
        for n in range(100, 1000):
            num1 = c * n
            num2 = reverse_number(num1)

            if num1 == num2 and largest_palindrome < num2:
                largest_palindrome = num2

    return largest_palindrome


def reverse_number(num):
    """(num) -> num

    Returns the reverse of a number.

    Keyword arguments:
    num -- Given number to reverse
    """

    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num = num // 10

    return reversed_num


print(largest_number_palindrome())
