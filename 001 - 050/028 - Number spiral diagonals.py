"""
Solution to
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def get_diagonals(n):
    res = [1]
    curr = 1
    incr = 2
    for _ in range(n//2):
        for _ in range(4):
            curr += incr
            res.append(curr)
        incr += 2
    return res


sol = sum(get_diagonals(1001))
print(sol)
