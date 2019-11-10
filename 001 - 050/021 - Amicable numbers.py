"""
Solution to
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt


def factors(n):
    limit = int(sqrt(n)) + 1
    res = []
    for i in range(1, limit):
        if n % i == 0:
            res.append(i)
            res.append(int(n / i))
    return sorted(res)


def find_amicable_pair(n):
    dn = factors(n)[0:-1]
    sdn = sum(dn)
    ddn = factors(sum(dn))[0:-1]
    sddn = sum(ddn)
    if n == sddn and sddn < sdn:
        return (sddn, sdn)
    else:
        return


pairs = [find_amicable_pair(x) for x in range(1, 10_000)]
sol = sum([x[0] + x[1] for x in pairs if x is not None])
print(sol)
