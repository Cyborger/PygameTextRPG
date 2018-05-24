class Inventory:
    def __init__(self):
        self.maxSize = 30
        self.items = []

    def getItems(self):
        return self.items

    def getWeapons(self):
        weaponList = []
        for item in self.items:
            if item.type == "Weapon":
                weaponList.append(item)
        return weaponList

    def addItem(self, item):
        self.items.append(item)
