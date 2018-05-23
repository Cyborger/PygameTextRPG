import pygame


class Location:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.mapLocation = jsonData["MapLocation"]
        self.connectedLocations = jsonData["ConnectedLocations"]
        self.image = "res/locationIcons/" + jsonData["Image"] + ".png"
        self.enemies = jsonData["Enemies"] if "Enemies" in jsonData else None

    def locationIsAdjacent(self, location):
        for direction in self.connectedLocations:
            if self.connectedLocations[direction] == location.name:
                return True
        return False

    def hasEnemies(self):
        if self.enemies is None:
            return False
        return True
