"""
Solution to
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


def tri(n):
    return [n * (n + 1) // 2 for n in range(1, n + 1)]


tris = tri(100)


def word_value(word):
    return sum([ord(chr) - 64 for chr in word])


def find_sol():
    res = 0
    with open("../res/p042_words.txt", "r") as f:
        words = f.readlines()[0].replace("\"", "").split(",")
        for word in words:
            if word_value(word) in tris:
                res += 1
    return res


sol = find_sol()
print(sol)
