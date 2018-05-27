class Item:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.value = 0


class Weapon(Item):
    def __init__(self, jsonData):
        super().__init__(jsonData)
        self.damage = jsonData["Damage"]


class Food(Item):
    def __init__(self, jsonData):
        super().__init__(jsonData)
        self.healing = jsonData["Healing"]
