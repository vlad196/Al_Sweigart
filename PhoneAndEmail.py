#! python3
# phoneAndEmail.py - Находит телефонные номера и
# адреса электроннлй почты в буфере обмена

import pyperclip
import re

phoneregex = re.compile(r'''(
    ([8]\s? | [+7]\s? | [7]\s?)
    (\d{3} | \(\d{3}\))?  # территориальный номер
    (\s |-|\.)?  # разделитель
    (\d{3})  # первые 3 цифры
    (\s |-|\.)  # разделитель
    (\d{4} | (\d{2}-\d{2}))  # последние 4 цифры или 2 через тирэ
    (\s*(ext |x| ext.) \s* (\d{2,5}))?  # добавочный номер
    )''', re.VERBOSE)

# Создание регулярных выражений для адрессов электронной почты.
emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # имя пользователя
    @  # символ @
    [a-zA-z0-9.-]+  # имя домена
    (\.[a-zA-z]{2,4})  # остальная часть адреса
    )''', re.VERBOSE)

# Поиск соответствий в тексе, содержавщемся в
# буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    phonenum = '-'.join([groups[1],groups[2],groups[4],groups[6]])
    if groups[8] != '':
        phonenum += 'x' + groups[8]
    matches.append(phonenum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

# Копирование результатов в буфере обмена.
if len(matches) > 0:
    pyperclip.copy('n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены')
