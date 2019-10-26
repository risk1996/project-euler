"""
Solution to
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

num_str = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    18: "eighteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    80: "eighty",
}


def num_to_words(n):
    if n == 0:
        return ""
    elif n in num_str:
        return num_str[n]
    elif 14 <= n <= 19:
        return num_str[n % 10] + "teen"
    elif 21 <= n <= 99:
        if n // 10 * 10 in num_str:
            return num_str[n // 10 * 10] + num_to_words(n % 10)
        else:
            return num_str[n // 10] + "ty" + num_to_words(n % 10)
    elif 100 <= n <= 999:
        return num_str[n // 100] + "hundred" + ("" if num_to_words(n % 100) == "" else "and" + num_to_words(n % 100))
    elif n == 1000:
        return "one" + "thousand"
    else:
        pass


num_words = [num_to_words(x) for x in range(1, 1001)]
sol = len("".join(num_words))
print(sol)
