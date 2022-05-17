#! python3
#! coding: utf-8

#printTable2.py - 2-ой вариант програмы, которая превращает список списков в список столбцов

tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colLen = len(data)
    rowLen = max(len(data[0]), len(data[colLen-1]))
    colWidths = []
    for i in range(colLen):
        colWidth1 = len(max(data[i], key=len))
        colWidths.append(colWidth1)
# Сделать новый список, где строка это новая часть столбца и вывести через join \t
    for row in range(rowLen):
        result = []
        for col in range(colLen):
            result.append(data[col][row].rjust(colWidths[col]))
        print('\t'.join(result))
printTable(tabledata)
