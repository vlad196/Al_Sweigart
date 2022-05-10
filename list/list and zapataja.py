#! python3
# -*- coding: utf-8 -*-
spam = ['яблоки', 'бананы', 'тофу', 'коты']
def listName(getList):
    line=''
    for i in range (len(getList) - 1):
        line = line + str(getList[i]) + ', '
    line = line + 'и ' + getList[-1]
    return line
print(listName(spam))