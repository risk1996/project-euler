"""
Solution to
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def name_list(filename):
    with open(filename, 'r') as f:
        raw_names = f.readline()
        name_arr = raw_names.split(',')
        clean_names = [name[1:-1] for name in name_arr]
        return clean_names


def name_score(i, name):
    chr_offset = ord('A') - 1
    name_chars = [ord(c) - chr_offset for c in name]
    return i * sum(name_chars)


sorted_name = sorted(name_list('../res/p022_names.txt'))
scores = [name_score(i + 1, name) for i, name in enumerate(sorted_name)]
sol = sum(scores)
print(sol)
