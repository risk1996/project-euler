"""
Solution to
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from math import sqrt
from bisect import bisect_left


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


prime_list = sieve(100_000)


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


def factors(n):
    limit = int(sqrt(n)) + 1
    res = []
    for i in range(1, limit):
        if n % i == 0:
            res.append(i)
            rem = int(n / i)
            if i != rem:
                res.append(int(n / i))
    return sorted(res)


def prime_factors(n):
    return [x for x in factors(n) if is_prime(x)]


def find_sol():
    count = 0
    for i in range(1, 1_000_000):
        pf = prime_factors(i)
        if len(pf) == 4:
            count += 1
        else:
            count = 0
        if count == 4:
            return i - 3


sol = find_sol()
print(sol)
