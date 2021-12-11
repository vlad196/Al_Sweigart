#! Python3
# -*- coding: utf-8 -*-

import random
secretNumber = random.randint(1, 20)
print("Я загадал число от 1 до 20.")

# Игроку даётся 6 попыток
for guessesTaken in range(1, 7):
    print("Угадайте число.")
    Guess = int(input())
    if guess < secretNumber:
        print("Я загадал большее число.")
    elif guess > secretNumber:
        print("Я загадал меньшее число.")
    else:
        break   # Число угадано!
if guess == secretNumber:
    print("Отлично! Количество попыток:" + str(guessesTaken) + ".")
else:
    print("Вам не повезло. Я загадал число " + str(secretNumber))
