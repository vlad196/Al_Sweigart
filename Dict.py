
Arnold = {"rope":1, "torch":6, "gold coin":42, "dagger":1,"arrow":12}
def displayinventory(NPC):
    for k, v in NPC.items():
        print(str(v) + " " + k)
    print("Total number of items:", sum(Arnold.values()))

displayinventory(Arnold)
