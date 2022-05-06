#-*- coding: utf-8 -*-


def displayInventory(NPC):
    print('Инвентарь:')
    itemTotal = 0
    for k , v in NPC.items():
        print(str(k) + ' - ' + str(v))
        itemTotal = itemTotal + 1


def newInventory(NPCinventory, addItems):
    addItemsDict = {}
    for items in addItems:
        addItemsDict.setdefault(items, 0)
        addItemsDict[items] = addItemsDict[items] + 1
    for k , v in addItemsDict.items():
        if k not in NPCinventory:
            NPCinventory.setdefault(k , 1)
        if k in NPCinventory:
            NPCinventory[k] = NPCinventory[k] + v
    return NPCinventory

inv = {'золотая монета': 42, 'веревка': 1}
dragonLoot = ['золотая монета', 'кинжал', 'золотая монета',
'золотая монета', 'рубин']
inv = newInventory(inv, dragonLoot)
displayInventory(inv)


checkRule = {'apple': 10, 'orange' : 3}
checkRule = checkRule['apple'] + 3
print('Всего яблок ' + str(checkRule))