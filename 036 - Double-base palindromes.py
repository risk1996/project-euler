"""
Solution to
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_palindrome(s):
    return s == s[::-1]


def binary(n):
    return bin(n)[2:]


sol = sum([
    x for x in range(1_000_000)
    if is_palindrome(str(x)) and is_palindrome(binary(x))
])
print(sol)
