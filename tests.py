import math

def displayInventory(inventory):
    print('Inventory')
    for k, v in inventory.items():
        print(v, k)
    print('Total number of items:' + ' ' + str(sum(inventory.values())))


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory[i] = inventory.get(i, 0) + 1
    return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)