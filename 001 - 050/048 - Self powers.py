"""
Solution to
Self powers
Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def find_sol():
    return sum([(i ** i) % (10 ** 10) for i in range(1, 1001)]) % (10 ** 10)


sol = find_sol()
print(sol)
