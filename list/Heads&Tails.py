#! python3
#-*- coding: utf-8 -*-
import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    headsAndTails = []
    for i in range(99):
        if random.randint(0,1) == 0:
            headsAndTails.append('орёл')
        else:
            headsAndTails.append('решка')
    for a in range(len(headsAndTails)-6):
        if headsAndTails[a:a+6] == ['решка', 'решка', 'решка', 'решка', 'решка', 'решка']\
                or headsAndTails[a:a+6] == ['орёл', 'орёл', 'орёл', 'орёл', 'орёл', 'орёл']:
            numberOfStreaks = numberOfStreaks + 1
        else:
            break
print(numberOfStreaks)
print('Вероятность появления серии: %s%%' % (numberOfStreaks / 100))

