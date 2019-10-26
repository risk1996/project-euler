"""
Solution to
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

triplet = [(a, b, 1000 - a - b) for a in range(1, 1001)
           for b in range(a, 1001) if a ** 2 + b ** 2 == (1000 - a - b) ** 2][0]
sol = triplet[0] * triplet[1] * triplet[2]
print(sol)
