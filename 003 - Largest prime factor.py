"""
Solution to
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def fact(n):
    limit = int(sqrt(n)) + 1
    res = []
    for i in range(1, limit):
        if n % i == 0:
            res.append(i)
            res.append(int(n / i))
    return res


def is_prime(n):
    return len(fact(n)) == 2


sol = max([x for x in fact(600851475143) if is_prime(x)])
print(sol)
