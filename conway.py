#! python3
# -*- coding: utf-8 -*-
# Игра жизнь

import random, time, copy

widht = 60
height = 20

# Создание списка списков для клеток
nextCells = []
for x in widht():
    column = [] # Создание нового столбца
    for y in height():
        if random.randint(0,1) == 0:
            column.append('#') # добавление жиавой клетки
        else:
            column.append(' ') # добавление мёртвой клетки
       nextCells.append(column) # добавление в основной список список столбцов

