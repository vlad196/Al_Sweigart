#! Python3

#  StatesAndCities - Преобразовывает строку штатов и городов в один словарь
import pyperclip
import re

#  Создаём правила регулярных выражений для ключа и значения
findstatescities = re.compile(r'(?P<state>[^\W\d_]+(?:\s+[^\W\d_]+)*)\s*\((?P<city>[^()]*)\)')
#  Сначала строка копирует строку
text = str(pyperclip.paste())

statescities = [x.groupdict() for x in re.finditer(findstatescities, text)]
print(statescities)


#  Создаём новый словарь
matches = {}
#  Регулярными выражениями в ключ добавляем города,
#  а в значение штаты

#  dict.update...добавлять в виде кортежа
#  Преобразуем в строку типа словаря

#  копируем
