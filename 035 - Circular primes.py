"""
Solution to
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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


prime_list = sieve(1_000_001)


def is_prime(n):
    return n in prime_list


def rotate_left(arr, n):
    n = n % len(arr)
    return arr[n:] + arr[:n]


def to_digits(n):
    return [int(x) for x in str(n)]


def from_digits(n):
    return int("".join([str(x) for x in n]))


def is_circular_prime(n):
    n_digits = to_digits(n)
    if n > 10 and len(set([0, 2, 4, 5, 6, 8]).intersection(n_digits)) > 0:
        return False
    for i in range(len(str(n))):
        if not is_prime(from_digits(rotate_left(n_digits, i))):
            return False
    return True


sol = len([x for x in range(2, 1_000_001) if is_circular_prime(x)])
print(sol)
