from lib.jsonLoader import JSONLoader
from core.item import Food, Weapon, CraftingItem

class ItemManager:
    def __init__(self):
        self.items = self.loadItems()

    def loadItems(self):
        items = []
        data = JSONLoader.getJSONData("items")
        for obj in data:
            itemData = data[obj]
            if itemData["Type"] == "Food":
                items.append(Food(itemData))
            elif itemData["Type"] == "Weapon":
                items.append(Weapon(itemData))
            elif itemData["Type"] == "Crafting":
                items.append(CraftingItem(itemData))
        return items

    def getItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                return item
        raise ItemNotFoundException(itemName)


class ItemNotFoundException(Exception):
    def __init__(self, itemName):
        super().__init__("Unable to find item: " + itemName)
