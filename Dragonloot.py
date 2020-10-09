def displayinventory(NPC):
    for k, v in NPC.items():
        print(str(v) + " " + k)
    print("Total number of items:", sum(NPC.values()))

def addToInventory(inventory, addedItems):
    count = {}
    for items in addedItems:
        count.setdefault(items, 0)
        count [items] = count[items] + 1
    print(count)
    inventory = {**inventory, **count}
    print(inventory)

inv = {"gold coin" : 42, "rope" : 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayinventory(inv)