"""
Solution to
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def nums():
    return [i * j for i in range(100, 1000) for j in range(100, 1000)]


def is_palindrome(n):
    return str(n) == str(n)[::-1]


sol = max([x for x in nums() if is_palindrome(x)])
print(sol)
