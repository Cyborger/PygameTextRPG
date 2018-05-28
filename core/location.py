import pygame
import random


class Location:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.mapLocation = jsonData["MapLocation"]
        self.connectedLocations = jsonData["ConnectedLocations"]
        self.image = "res/locationIcons/" + jsonData["Image"] + ".png"
        self.canRest = jsonData["CanRest"] if "CanRest" in jsonData else False
        self.canMine = jsonData["CanMine"] if "CanMine" in jsonData else False
        self.boss = jsonData["Boss"] if "Boss" in jsonData else None
        self.enemies = jsonData["Enemies"] if "Enemies" in jsonData else None

    def locationIsAdjacent(self, location):
        for direction in self.connectedLocations:
            if self.connectedLocations[direction] == location.name:
                return True
        return False

    def hasEnemies(self):
        if self.enemies is not None or self.boss is not None:
            return True
        return False

    def getEnemyEncounter(self):
        enemies = []
        if self.boss is not None:
            enemies.append(self.boss)
        else:
            roll = random.randint(0, 5)
            enemies.append(self.getRandomEnemy())
            if roll < 3:
                enemies.append(self.getRandomEnemy())
            if roll == 0:
                enemies.append(self.getRandomEnemy())
        return enemies

    def getRandomEnemy(self):
        return random.choice(self.enemies)
