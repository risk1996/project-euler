"""
Solution to
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

d_2 d_3 d_4 = 406 is divisible by 2
d_3 d_4 d_5 = 063 is divisible by 3
d_4 d_5 d_6 = 635 is divisible by 5
d_5 d_6 d_7 = 357 is divisible by 7
d_6 d_7 d_8 = 572 is divisible by 11
d_7 d_8 d_9 = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


def satisfy_property(digits):
    if int(digits[1] * 100 + digits[2] * 10 + digits[3]) % 2 != 0:
        return False
    if int(digits[2] * 100 + digits[3] * 10 + digits[4]) % 3 != 0:
        return False
    if int(digits[3] * 100 + digits[4] * 10 + digits[5]) % 5 != 0:
        return False
    if int(digits[4] * 100 + digits[5] * 10 + digits[6]) % 7 != 0:
        return False
    if int(digits[5] * 100 + digits[6] * 10 + digits[7]) % 11 != 0:
        return False
    if int(digits[6] * 100 + digits[7] * 10 + digits[8]) % 13 != 0:
        return False
    if int(digits[7] * 100 + digits[8] * 10 + digits[9]) % 17 != 0:
        return False
    return True


def get_pandigitals():
    return [x for x in permutations(range(10)) if x[0] != 0]


def from_digits(arr):
    return int("".join([str(x) for x in arr]))


def find_sol():
    return sum([from_digits(x) for x in get_pandigitals() if satisfy_property(x)])


sol = find_sol()
print(sol)
