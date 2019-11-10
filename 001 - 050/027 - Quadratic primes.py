"""
Solution to
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:
n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from math import sqrt


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


def is_prime(n):
    return len(factors(n)) == 2


def quadratic_consecutive_primes(a, b):
    for i in range(10 ** 1000):
        quadratic = i * i + a * i + b
        if quadratic <= 0 or not is_prime(quadratic):
            return i - 1


consecutive_primes = [
    (quadratic_consecutive_primes(a, b), a, b)
    for a in range(-999, 1000)
    for b in range(-1000, 1001)
]
max_cp = max(consecutive_primes)
sol = max_cp[1] * max_cp[2]
print(sol)
