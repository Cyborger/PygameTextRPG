class Item:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.type = jsonData["Type"]
        self.damage = jsonData["Damage"] if "Damage" in jsonData else None
