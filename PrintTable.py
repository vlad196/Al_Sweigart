#! python3
# PrintTable.py - Выводит список в ровной таблице

tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# manipulating strings 143

'''def printtable(data):
    for i in range(len(data)):
        colwights = [0] * len(data)
        print(colwights)'''

# как должно быть


def printtable(data):
    cols = len(data)
    rows = len(data[0])

    col_width = []
    for col in data:
        col_width.append(len(sorted(col, key=len)[-1]))

    for row in range(rows):
        result = []
        for col in range(cols):
            result.append(data[col][row].rjust(col_width[col]))
        print('\t'.join(result))


printtable(tabledata)
