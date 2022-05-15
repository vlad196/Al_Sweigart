#! python3
# -*- coding: utf-8 -*-

# pigLatin.py - программа, которая преобразует английский текст в текст на поросячем языке

message = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
pigLatin = [] # список слов на поросячем языке
for word in message.split():
    # отделяем небуквенные символы в начале слова
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
    # отделяем небуквенные символы в начале слова
    sufixNonLetters = ''
    while not word[-1].isalpha():
        sufixNonLetters += word[-1]
        word = word[:-1]
    # запоминанем регистр слова
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    # перевод в нижний регистр
    word = word.lower()
    # отделяем согласные в начале слова
    prefixConsonant = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonant += word[0]
        word = word[1:]
    if prefixConsonant != '':
        word += prefixConsonant + 'ay'
    else:
        word += 'yay'
    # возвращаем исходный регистр
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    # возвращаем небуквенные символы в начало и конец слова
    pigLatin.append(prefixNonLetters + word + sufixNonLetters)
# соединяем слова обратно в текст
print(''.join(pigLatin))