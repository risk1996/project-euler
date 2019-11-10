"""
Solution to
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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


def is_truncatable_prime(n):
    str_n = str(n)
    if n <= 7 or not is_prime(n):
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True


def find_sol():
    res = set()
    appends = ['1', '3', '7', '9']
    queue = [2, 3, 5, 7]
    while len(queue) > 0:
        curr = queue.pop(0)
        for append in appends:
            app_left = int(append + str(curr))
            app_right = int(str(curr) + append)
            if is_prime(app_left):
                queue.append(app_left)
                if is_truncatable_prime(app_left):
                    res.add(app_left)
            if is_prime(app_right):
                queue.append(app_right)
                if is_truncatable_prime(app_right):
                    res.add(app_right)
    return sum(list(res))


sol = find_sol()
print(sol)
