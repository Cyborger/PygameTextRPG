class Inventory:
    def __init__(self):
        self.maxSize = 30
        self.items = []
        self.gold = 0

    def getItems(self):
        return self.items

    def addItems(self, *items):
        for item in items:
            self.items.append(item)
