"""
Solution to
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from fractions import Fraction


def to_digit_str(n):
    return [x for x in str(n)]


def from_digit_str(n):
    return int("".join(n))


def find_sol():
    res = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if i % 10 == 0 or j % 10 == 0:
                continue
            num, den = set(to_digit_str(i)), set(to_digit_str(j))
            s_num, s_den = num - den, den - num
            si_num = from_digit_str(list(s_num) or ['0'])
            si_den = from_digit_str(list(s_den) or ['0'])
            if si_den == 0 or Fraction(i, j) != Fraction(si_num, si_den):
                continue
            if len(num.intersection(den)) != 1:
                continue
            res *= Fraction(i, j)
    return res.denominator


sol = find_sol()
print(sol)
