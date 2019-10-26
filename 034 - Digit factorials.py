"""
Solution to
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def to_digits(n):
    return [int(x) for x in str(n)]


def find_sol():
    res = []
    for i in range(10, 100_000):
        if sum([factorial(x) for x in to_digits(i)]) == i:
            res.append(i)
    return sum(res)


sol = find_sol()
print(sol)
