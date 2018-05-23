class Enemy:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.maxHealth = jsonData["Health"]
        self.currentHealth = self.maxHealth
