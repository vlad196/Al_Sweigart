#! python3
#-*- coding: utf-8 -*-

allGuests = [('Alice', {'apples': 5, 'pretzels': 12}, 'acc'),
             ('Bob', {'ham sandwiches': 3, 'apples': 2}, 'bcc'),
             ('Carol', {'cups': 3, 'apple pies': 1}, 'ccc'),
             ('Carol2', {'cups2': 3, 'apple pies2': 1}, 'dcc')]

def totalBrought(guests, item):
    numBrought = 0
    for k, v, c in guests:
        print(guests)
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))