"""
Solution to
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

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


prime_list = sieve(10_000)


def to_digits(n):
    return [int(x) for x in str(n)]


def from_digits(n):
    return int("".join([str(x) for x in n]))


def find_sol():
    res = set()
    for prime in prime_list:
        if prime >= 1000:
            perms = [from_digits(x) for x in permutations(to_digits(prime))]
            perms = [x for x in perms if x >= 1000]
            prime_perms = set(perms).intersection(prime_list)
            if len(prime_perms) >= 3:
                prime_tuple = tuple(sorted(list(prime_perms)))
                for i in range(2, len(prime_tuple)):
                    for j in range(1, i):
                        for k in range(j):
                            if prime_tuple[i] - prime_tuple[j] == \
                                    prime_tuple[j] - prime_tuple[k]:
                                res.add((
                                    prime_tuple[k],
                                    prime_tuple[j],
                                    prime_tuple[i],
                                ))
    return max([from_digits(x) for x in res])


sol = find_sol()
print(sol)
