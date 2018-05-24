class Item:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.type = jsonData["Type"]
