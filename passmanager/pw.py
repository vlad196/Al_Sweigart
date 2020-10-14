#! python3
# pw.py - Программа для незащищенного хранения паролей

PASSWORDS = {'email': 'onetwothree',
             'blog': 'Vasilij12',
             'luggage': '12345'}

import pyperclip
import sys

if len(sys.argv) < 2:
    print('использование: python pw.py [имя учетной записи] - '
          'копирование пароля учетной записи')
    sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])  # значит питоон умеет выводить не только индексу,
    # но и по самому названию
    print('Пароль для + account' + ' скопирован в буфер обмена')
else:
    print('Учетная запись' + account + ' отсутствует в списке')
