"""
Solution to
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""


def fact(n):
    limit = int(n ** (1/2)) + 1
    res = []
    for i in range(1, limit):
        if n % i == 0:
            res.append(i)
            res.append(int(n / i))
    return res


def tri(n):
    return int(n * (n+1) / 2)


def find_sol():
    for i in range(7, 1_000_000):
        num = tri(i)
        if len(fact(num)) > 500:
            return num


sol = find_sol()
print(sol)
