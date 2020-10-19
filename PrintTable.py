#! python3
# PrintTable.py - Выводит список в ровной таблице

tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# manipulating strings 143 для чего это в книжке?...

def printtable(data):  # Создаём функцию, где:
    cols = len(data)  # Число колонок это кол-во объектов в списке data
    rows = len(data[0])  # Число строк это кол-во объектов в 1-м списке списка data (неуниверсально.
    # Можно сделать в зависимости от максимума в строке объектов

    col_wigth = []  # Новый список, отвечающий за ширину
    # Цикл for это поочередный перебор объекта (col) из объекта (data).
    # перебирает разный по весу горох в одном стручке и выдаёт массу каждого гороха по очереди. (как пример)
    # а если там range(), то это расчёт в диапазоне кол-ва гороха
    for col in data:  # создаём цикл значений col из data
        col_wigth.append(len(sorted(col, key=len)[-1]))  # В спискок col_wight вставляем колличество символов
        # последнего объекта (col) из списка [-1] отсортированного по длинне символов sorted key = len

    for row in range(rows):  # создаём цикл значений row из диапазона значений rows
        result = []  # Новый список для каждой строки
        for col in range(cols):  # создаём цикл значений col  диапазоне значений cols
            result.append(data[col][row].rjust(col_wigth[col]))  # к списку result добавляем значение списка row
            # из списка col,где справа rjust добавляет пробелы равные значению col из списка col_wight
        print('\t'.join(result))  # Списки соединяем в строки с горизонтальными табуляциями
        # (можно было и пробелами но так лучше)


printtable(tabledata)
