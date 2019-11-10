"""
Solution to
Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""


def tri(n):
    return [n * (n + 1) // 2 for n in range(1, n + 1)]


def pent(n):
    return [n * (3 * n - 1) // 2 for n in range(1, n + 1)]


def hexa(n):
    return [n * (2 * n - 1) for n in range(1, n + 1)]


def find_sol(limit):
    tris_set = set(tri(limit))
    pents_set = set(pent(limit))
    hexas_set = set(hexa(limit))
    intersection = tris_set.intersection(pents_set).intersection(hexas_set)
    return intersection


sol = find_sol(1_000_000)
print(sol)
