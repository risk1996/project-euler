"""
Solution to
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


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


sol = sum(sieve(2_000_000))
print(sol)
