__author__ = 'Sumanth_Lingappa'

'''
count the number of days between two dates.
Ref : www.geeksforgeeks.org/find-number-of-days-between-two-given-dates/
'''


class Date(object):
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year


month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leapYearCount(d):

    year = d.year

    if d.month <= 2:
        year -= 1

    count = year/4 - year/100 + year/400
    return count

def numOfDays(d1, d2):
    numDay1 = d1.date + sum(month[0:d1.month]) + d1.year * 365
    numDay2 = d2.date + sum(month[0:d2.month]) + d2.year * 365

    numDay1 += leapYearCount(d1)
    numDay2 += leapYearCount(d2)

    return abs(numDay1 - numDay2)


d1 = Date(1, 02, 2000)
d2 = Date(1, 02, 2004)

print numOfDays(d1, d2)
