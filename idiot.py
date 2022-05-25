#! python3
#-*-coding: utf-8 -*-

#idiot.py - программа ,которая будет проверять введённый тип данных
# и возвращать ответ, в зависимоти от да или нет

import pyinputplus as pyip

while True:
    prompt = 'Хотите узнать, как занять дурака на несколько часов?'
    responce = pyip.inputYesNo(prompt)
    if responce == 'no':
        break
print('Спасибо')