"""
Solution to
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def is_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a > 0 and a * a + b * b == c * c


def triplet_count_for_perimeter(n):
    res = set()
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            if is_pythagorean_triplet(i, j, n - i - j):
                res.add(tuple(sorted([i, j, n - i - j])))
    return len(res)


sol = max([(triplet_count_for_perimeter(x), x) for x in range(3, 1001)])[1]
print(sol)
