import pygame


class PlayerClass:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.description = jsonData["Description"]

    def getIcon(self):
        return pygame.image.load("res/classIcons/" + self.name + ".png")

    @classmethod
    def getDefaultPlayerClass(cls):
        return PlayerClass({"Name" : "Default", "Description" : ""})
