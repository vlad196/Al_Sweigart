# -*- coding: UTF-8 -*-
#!  python3
#  mcb.pyw - Сохраняет и загружает фрагменты
#  текста в буфер обмена
#  Использование: py.exe mcb.pyw save <Ключевое слово. -
#  Сохраняет буфер обмена в ключевое слово.
#  py.exe mcb.pyw <ключевое слово> -
#  Загружает ключевое слово в буфер обмена.
#  py.exe mcb.pyw list -
#  Загружает все ключевые слова в буфер обмена.

import shelve, pyperclip, sys

mcbshelf = shelve.open('')
#  Сохранить содержимое в буфер обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #  Сформировать список ключевых слов и загрузить содержимое.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbshelf.clear()
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()

