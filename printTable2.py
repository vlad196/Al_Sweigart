#! python3
#! coding: utf-8

#printTable2.py - 2-ой вариант програмы, которая превращает список списков в список столбцов

tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# Сделать подсчёт самого длинного списка в списке для того, чтобы узнать какой длинны должна быть строка

# Сделать подсчёт столбцов и строк

# Сделать новый список, где строка это новая часть столбца и вывести через join \t
def printTable(data):
    colWidth = [0]* len(data)
    print(colWidth)


printTable(tabledata)
