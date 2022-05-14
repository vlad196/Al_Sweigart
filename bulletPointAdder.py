#! python3
# coding: utf-8

#bulletPointAdder.py - дбоавляет звёздочку в начле каждой новой строки и возвращает это в буфер обмена

import pyperclip

text = pyperclip.paste()
# добавление звёздочки с кадой новой строки
lines = text.split('\n') # Из элемента строки сделал список через \n
for i in range(len(lines)): # в колличестве элементов списка поочередно выбрать элемент
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines) # Соединил список в один элемент через \n
pyperclip.copy(text)
print(text)

