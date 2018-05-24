class Item:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.type = jsonData["Type"]
        self.damage = 0 if "Damage" not in jsonData else jsonData["Damage"]
