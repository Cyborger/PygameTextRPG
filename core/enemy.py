class Enemy:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.maxHealth = jsonData["Health"]
        self.currentHealth = self.maxHealth

    def takeDamage(self, damage):
        self.currentHealth = max(self.currentHealth - damage, 0)

    def isDead(self):
        if self.currentHealth == 0:
            return True
        return False
