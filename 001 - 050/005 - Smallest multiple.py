"""
Solution to
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            return a


sol = 1
for i in range(2, 21):
    sol = int(sol * i / gcd(sol, i))
print(sol)
