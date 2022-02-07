#! Python3
# -*- coding: utf-8 -*-

import random, sys
print("Камень, ножницы, бумага")
#   В этих переменных накапливается количество очков
wins = 0
losses = 0
ties = 0
# далее будем вводить главное тело приложения стр 97
# Добавление переменной значения игрока и функцию выхода, если выбрать "в"
while True:
    #print(str(wins) + "побед",)
    print('%s побед, %s поражений, %s ничьих' % (wins, losses, ties))
    """это можно заменить на print(str(wins) + "побед",...), %s забирает числовое значение(s) из кортежа %"""
    """Сам кортеж может представлять переменные с их значениями, т.е. "wins" это тот же "wins" выше"""
    while True:
        print("Выберите ход (к) камень, (н) ножницы, (б) бумага, (в) выход")
        playerMove = input()
        if playerMove == "в":
            sys.exit()
        if playerMove == "к" or playerMove == "н" or playerMove == "б":
            break
        print("Введите 'к', 'н', 'б' или 'в'")
    """выводим что выбрал игрок"""
    if playerMove == "к":
        print("вы выбрали камень")
    if playerMove == "н":
        print("вы выбрали ножницы")
    if playerMove == "б":
        print("вы выбрали бумагу")
    """выбор компа и вывод результата"""
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computeNumber = "к"
        print("Компьютер выбрал камень")
    if randomNumber == 2:
        computeNumber = "н"
        print("Компьютер выбрал ножницы")
    elif randomNumber == 3:
        computeNumber = "б"
        print("Компьютер выбрал бумагу")
    """Логика подсчёта и подсчёт результата"""
    if playerMove == computeNumber:
        print("Ничья")
        ties = ties + 1
    if playerMove == "к" and computeNumber == "н":
        print("Вы выиграли")
        wins = wins + 1
    if playerMove == "н" and computeNumber == "б":
        print("Вы выиграли")
        wins = wins + 1
    if playerMove == "б" and computeNumber == "к":
        print("Вы выиграли")
        wins = wins + 1
    if playerMove == "н" and computeNumber == "к":
        print("Вы проиграли")
        losses = losses + 1
    if playerMove == "к" and computeNumber == "б":
        print("Вы проиграли")
        losses = losses + 1
    elif playerMove == "б" and computeNumber == "н":
        print("Вы проиграли")
        losses = losses + 1