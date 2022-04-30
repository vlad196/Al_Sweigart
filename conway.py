#! python3
# -*- coding: utf-8 -*-
# Игра жизнь
import random, time, copy
width = 60
height = 20

# Создание списка списков для клеток
nextCells = []
for x in range(width):
    column = [] # Создание нового столбца
    for y in range(height):
        if (x, y) in ((1, 0), (2, 1), (0, 2),(1, 2), (2, 2)):
            column.append('#') # Добавление жиавой клетки
        else:
            column.append(' ') # добавление мёртвой клетки
    nextCells.append(column) # добавление в основной список список столбцов

# Основной цикл
while True:
    print('\n\n\n\n\n') #отделим каждый шаг игры с помошью символов новой строки
    currentCells = copy.deepcopy(nextCells)

    # Вывод текущих клеток на экран
    for y in range(height):
        for x in range(width):\
            print(currentCells[x][y], end=' ')
        print() #Вывод символа новой строки в конце
# Отсюда мы уже выводим изображение клеток с рандомным содержимым
    #Вычисление клеток на следующем шаге на основе клеток текущего шага
    for x in range(width):
        for y in range(height):
            # Получение соседних координат
            # Выражение ’% WIDTH' гарантирует, что значение
            # leftCoord всегда находится между 0 и WIDTH - 1
            leftCoord =  (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            # Вычисление количества живых соседних клеток
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка
                                # слева сверху
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка сверху
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка
                                    # справа сверху
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # жива соседняя клетка слева
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # жива соседняя клетка справа
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка
                                    # слева снизу
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка снизу
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # жива соседняя клетка
                                    # справа снизу
            # Изменение клетки на основе правил игры
            if currentCells [x][y] == '#' and numNeighbors == 2 or numNeighbors == 3:
                # Живые клетки с двумя или тремя живыми
                # соседями остаются живыми
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Мёртвые клетки с тремя живыми соседями оживают
                nextCells[x][y] = '#'
            else:
                # Все остальные погибают или остаются мёртвыми
                nextCells[x][y] = ' '
time.sleep(1)