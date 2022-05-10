#! python3
# -*- coding: utf-8 -*-


def printPicnic(itemsDict, leftWidth, righrWidth):
    print('БЕРЁМ НА ПИКНИК'.center(leftWidth + righrWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(righrWidth))

picnicItems = {'сендвичи': 4, 'яблоки': 12, 'чашки': 4, 'печенье': 8000}
printPicnic(picnicItems, 16, 5)
printPicnic(picnicItems, 24, 7)