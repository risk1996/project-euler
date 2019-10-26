"""
Solution to
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def champernowne_constant(limit):
    res = ""
    for i in range(1_000_000):
        res += str(i)
        if len(res) >= limit:
            return res


def prod(arr):
    res = 1
    for item in arr:
        res *= item
    return res


const = champernowne_constant(1_000_001)
sol = prod([int(const[10 ** x]) for x in range(7)])
print(sol)
