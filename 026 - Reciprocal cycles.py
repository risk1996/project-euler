"""
Solution to
Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from math import log10


def calc_cycle(n):
    den = 10 ** int(log10(n) + 1)
    decs = []
    while True:
        q, r = divmod(den, n)
        if r == 0:
            return 0
        else:
            if q in decs:
                return len(decs) - decs.index(q)
            else:
                decs.append(q)
        den = r * 10 ** int(log10(n) + 1)


sol = max([(calc_cycle(n), n) for n in range(1, 1000)])[1]
print(sol)
