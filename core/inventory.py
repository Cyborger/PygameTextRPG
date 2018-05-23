class Inventory:
    def __init__(self):
        self.maxSize = 30
        self.items = []

    def getItems(self):
        return self.items
        
    def addItem(self, item):
        self.items.append(item)
