#! Python3

# -*- coding: utf-8 -*-

# Игра жизнь

import random, time, copy

widht = 60
height = 20

# Создание списка списков для клеток
for x in widht():
    column = [] #Создание нового столбца
    for y in height():
        if random.randint(0,1) == 0:
            pass