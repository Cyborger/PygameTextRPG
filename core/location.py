import pygame


class Location:
    locationImages = {"Resting" : "campfire", "Forest" : "forest"}

    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.image = self.loadImage(jsonData["Type"])

    def loadImage(self, locationType):
        imagePath = "res/images/" + self.locationImages[locationType] + ".png"
        return pygame.image.load(imagePath)
