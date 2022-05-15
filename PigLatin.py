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
