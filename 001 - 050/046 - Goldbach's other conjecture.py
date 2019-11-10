"""
Solution to
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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


prime_list = sieve(100_000)


def find_sol():
    constructible = []
    for prime in prime_list:
        for i in range(1, 300):
            constructible.append(prime + 2 * i * i)
    return min(set(range(3, 100_000, 2)) - set(prime_list) - set(constructible))


sol = find_sol()
print(sol)
