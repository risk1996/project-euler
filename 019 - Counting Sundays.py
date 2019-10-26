"""
Solution to
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.
 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_days(month, year):
    days = [31, 28 + (1 if is_leap_year(year) else 0), 31,
            30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month]


def partial_sum(arr):
    res = [0]
    for i in range(1, len(arr)):
        res.append(res[i-1] + arr[i-1])
    return res


first_dates = partial_sum([get_days(mo, yr) for yr in range(1901, 2001)
                           for mo in range(12)])
# 1 January 1901 is Tuesday
sol = len([x for x in first_dates if x % 7 == 5])
print(sol)
