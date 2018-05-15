import pygame


class Location:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.releventImage = {"Resting" : "campfire", "Forest" : "forest"}
        self.image = self.loadImage(jsonData["Type"])

    def loadImage(self, locationType):
        imagePath = "res/images/" + self.releventImage[locationType] + ".png"
        return pygame.image.load(imagePath)
