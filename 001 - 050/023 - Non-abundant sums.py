"""
Solution to
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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


def is_abundant(n):
    return n < sum(factors(n)[:-1])


def find_sol():
    ints = [False for x in range(30_000)]
    abundants = [x for x in range(12, 30_000) if is_abundant(x)]
    for i in abundants:
        for j in abundants:
            if i + j < 30_000:
                ints[i + j] = True
    return sum([i for i in range(0, 30_000) if not ints[i]])


sol = find_sol()
print(sol)
