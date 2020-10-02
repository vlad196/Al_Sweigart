# spam = ['a','b','c','d']
# print(spam[int('3'* 2) / 11])

# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.index('cat'))
# bacon.append(99)
# bacon.insert(2, 228)
# print(bacon)
# bacon.remove('cat')
# print(bacon)


# def kkk(need):
# a = ', '.join(need)
# spam = a.replace(',',' and', ) #Нужно наоборот, чтобы было вконце. Может нужен другой подход?
# Может как то с строкой управлять как списком?
# return spam
def kek(lst):
    a = ' , '.join(lst)  # apples , bananas , tofu , cats
    # делает список
    b = a.rsplit(' , ', 1)  # ['apples , bananas , tofu', 'cats']
    # разбивает по последнему знаку и делает 2 разных значения списка
    c = ' and '.join(b)  # apples , bananas , tofu and cats
    # заменяет знак на and и вохвращает строку
    # B = ' and '.join(' , '.join(lst).rsplit(' , ', 1)) #не понял как это работает
    return c


spam = ['apples', 'bananas', 'tofu', 'cats']
print(kek(spam))
