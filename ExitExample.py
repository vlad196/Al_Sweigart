#! Python3
# -*- coding: utf-8 -*-

import sys
while True:
    print("Введите слово ""Exit""")
    responce = input()
    if responce == "Exit":
        sys.exit()
    print("вы ввели " + responce +".")
