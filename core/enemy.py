import random


class Enemy:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.currentHealth = jsonData["Health"]
        self.maxHealth = jsonData["Health"]
        self.goldDrop = jsonData["GoldDrop"]
        self.dropChances = jsonData["DropChances"]

    def takeDamage(self, damage):
        self.currentHealth = max(self.currentHealth - damage, 0)

    def isDead(self):
        if self.currentHealth == 0:
            return True
        return False

    def calculateGoldDrop(self):
        roll = random.randint(self.goldDrop[0], self.goldDrop[1])
        return roll

    def calculateItemDrops(self):
        drops = []
        roll = random.randint(0, 100)
        for drop in self.dropChances:
            if roll < self.dropChances[drop]:
                drops.append(drop)
        return drops
