"""
Solution to
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations

# def is_pandigital(m1, m2, prod):
# return sorted([int(x) for x in str(m1)]) == range()


def check_identity(arr):
    perms = permutations(arr)
    elems = len(arr)
    res = set()
    for perm in perms:
        for mul in range(1, elems - 1):
            for eq in range(mul + 1, elems):
                multiplicand = int("".join([str(x) for x in perm[:mul]]))
                multiplier = int("".join([str(x) for x in perm[mul:eq]]))
                product = int("".join([str(x) for x in perm[eq:]]))
                if multiplicand * multiplier == product:
                    res.add(product)
    return list(res)


sol = sum(check_identity(range(1, 10)))
print(sol)
