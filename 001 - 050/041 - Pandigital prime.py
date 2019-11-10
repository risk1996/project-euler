"""
Solution to
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from bisect import bisect_left
from itertools import permutations


def sieve(limit):
    primes = [True for x in range(limit)]
    primes[0] = primes[1] = False
    res = []
    for i in range(2, limit):
        if primes[i]:
            res.append(i)
            for j in range(i * i, limit, i):
                primes[j] = False
    return res


prime_list = sieve(9_000_000)


def bin_search(haystack, needle):
    i = bisect_left(haystack, needle)
    if i != len(haystack) and haystack[i] == needle:
        return i
    raise ValueError


def is_prime(n):
    try:
        bin_search(prime_list, n)
        return True
    except ValueError:
        return False


def from_digits(arr):
    return int("".join([str(x) for x in arr]))


def get_pandigital_numbers(n):
    return [from_digits(num) for num in permutations(range(1, n + 1))]


def find_sol():
    for i in range(7, 0, -1):
        for num in reversed(list(get_pandigital_numbers(i))):
            if is_prime(num):
                return num


sol = find_sol()
print(sol)
