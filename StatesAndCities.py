#! Python3

#  StatesAndCities - Преобразовывает строку штатов и городов в один словарь
import pyperclip
import re

#  Создаём правила регулярных выражений для ключа и значения
states = re.compile('''(
    (?!=[(])
    [А-Яа-я\s]+)
    ''', re.VERBOSE)
cities = re.compile('''(
  (?<=[(])
  [А-Яа-я\s]+)''', re.VERBOSE)
#  Сначала строка копирует строку
text = str(pyperclip.paste())

print(states.findall(text))
print(cities.findall(text))

#  Создаём новый словарь
matches = {}
#  Регулярными выражениями в ключ добавляем города,
#  а в значение штаты
for statescities in
#  dict.update...добавлять в виде кортежа
#  Преобразуем в строку типа словаря

#  копируем
