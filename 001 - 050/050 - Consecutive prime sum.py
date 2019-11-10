"""
Solution to
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

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


prime_list = sieve(1_000_000)


def partial_sum(arr):
    res = [0]
    for i in range(1, len(arr)):
        res.append(res[i-1] + arr[i-1])
    return res


prime_partial_sum = partial_sum(prime_list)


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


def find_sol(limit):
    res = []
    for i in range(1, len(prime_list)):
        for k in range(i):
            prime_sum = prime_partial_sum[i] - prime_partial_sum[k]
            if prime_sum > limit:
                break
            if is_prime(prime_sum):
                res.append(prime_sum)
    return max(res)


sol = find_sol(1_000_000)
print(sol)
