#! Python3

#  StatesAndCities - Преобразовывает строку штатов и городов в один словарь
import pyperclip
import re

#  Создаём правила регулярных выражений для ключа и значения
findstatescities = re.compile(r'''(
    ([^\W\d_]+(?:\s+[^\W\d_]+)*)
    \s*\(([^()]*)\)
    )''', re.VERBOSE)
#  Сначала строка копирует строку
text = str(pyperclip.paste())
matches1 ={}
for groups in findstatescities.findall(text):
    matches1.update({groups[1]:groups[2]})
print(matches1)
#  Создаём новый словарь
#  Регулярными выражениями в ключ добавляем города,
#  а в значение штаты

#  dict.update...добавлять в виде кортежа
#  Преобразуем в строку типа словаря

#  копируем
