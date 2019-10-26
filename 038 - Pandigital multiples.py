"""
Solution to
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(n):
    str_n = str(n)
    return len(str_n) == 9 and set([int(x) for x in str_n]) == set(range(1, 10))


def concat_multiple(n):
    res = ""
    for i in range(100):
        res += str(i * n)
        if int(res or 0) > 10 ** 8:
            return int(res)


def find_sol(limit):
    concats = [concat_multiple(n) for n in range(1, limit)]
    # print(concats)
    concats = [x for x in concats if is_pandigital(x)]
    # print(concats)
    return max(concats)


sol = find_sol(10_001)
print(sol)
