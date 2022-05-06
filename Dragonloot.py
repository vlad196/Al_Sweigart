def displayinventory(npc):  # Сама функция инвентаря
    for k, v in npc.items():  # создаём цикл for для переменных key(ключа) и value(значения)
        # в диапазоне "предметов"(пар слов) словаря
        print(str(v) + " " + k)  # выводим в виде строки value(значение) + key(ключ, т.е. сам предмет)
    print("Total number of items:", sum(npc.values()))  # Выводим сумму значений value словаря


def addtoinventory(inventory, addeditems):  # функция добавления списка лута в словарь инвентаря
    dictloot = {}  # Сначала создаём пустой словарь для лута
    for items in addeditems:  # чтобы перенести список в словарь
        # создаём цикл для переменной items в диапазоне списка
        dictloot.setdefault(items, 0)  # используем метод .setdefault на пустом словаре.
        # (items это значения списка, выводящиеся по порядку в диапазоне самого списка addeditems)
        # Если новый предмет, то добавляем его в словарь и даём значение 0 (там все добавляются)
        dictloot[items] = dictloot[items] + 1  # Если уже есть пара ключа значения, то добавляем + 1
    for k, v in dictloot.items():  # Тут добавляем значения одного словаря в другой
        # создаём цикл с переменными key и value в диапазоне пары ключей значений в словаре dictloot
        if k not in inventory:  # Если key предмета нет в словаре инвентаря
            inventory.setdefault(k, 1)  # То добавляем его со значением 1
        elif k in inventory:  # Илиесли key предмет есть в инвентаре
            inventory[k] = inventory[k] + v  # То добавляем к !!!определённому!!! в итеррации цикла
            # key предмету v значение
    return inventory  # обязательно возвращвем полученный и нужгный нам словарь, иначе будет возвращено none!


inv = {"gold coin": 42, "rope": 1}  # Изначально у нас есть инвентарь из словаря
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]  # Dу нас есть лут из списка
inv = addtoinventory(inv, dragonLoot)  # Переадресуем переменнную на обновлённый словарь, после функции
displayinventory(inv)  # Выводим инвентарь на дисплей
