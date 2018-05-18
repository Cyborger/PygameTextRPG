import pygame
from core.menu import Menu
from core.gui.surface import Surface
from core.gui.imageButton import ImageButton
from core.gui.label import Label


class TravelMenu(Menu):
    def __init__(self, parentState):
        super().__init__("travelMenu", parentState)

    def isNowCurrentMenu(self):
        self.createBackground()
        self.createButtons()
        self.createLabels()

    def render(self):
        for surface in self.surfaces:
            self.draw(surface.image, surface.rect)
        for guiElement in self.buttons + self.labels:
            self.draw(guiElement.image, guiElement.rect)

    def createBackground(self):
        image = pygame.Surface((700, 700))
        for location in self.getParent().locations:
            for direction in location.connectedLocations:
                locationName = location.connectedLocations[direction]
                connectedLocation = self.getParent().getLocation(locationName)
                start = location.mapLocation
                start = [start[0], start[1]]
                end = connectedLocation.mapLocation
                end = [end[0], end[1]]
                pygame.draw.line(image, (255, 255, 255), start, end, 3)
        self.addSurfaces(Surface(image, 0, 0))

    def createButtons(self):
        # Create all the location buttons and the back button
        buttonImage = pygame.image.load("res/images/mapButtonDefault.png")
        buttonImageCurrent = pygame.image.load("res/images/" +
                                               "mapButtonCurrent.png")
        buttonImageHovered = pygame.image.load("res/images/" +
                                               "mapButtonHovered.png")

        for location in self.getParent().locations:
            x, y = location.mapLocation
            if location == self.getParent().currentLocation:
                self.addButtons(ImageButton(buttonImageCurrent,
                                            buttonImageCurrent, x - 16, y - 16,
                                            self.locationChosen, location))
            else:
                self.addButtons(ImageButton(buttonImage, buttonImageHovered,
                                            x - 16, y - 16,
                                            self.locationChosen, location))

    def createLabels(self):
        for location in self.getParent().locations:
            newLabel = Label(location.name, 0, 0, fontSize=16)
            newLabel.rect.centerx = location.mapLocation[0]
            newLabel.rect.bottom = location.mapLocation[1] - 24
            background = pygame.Surface((newLabel.rect.width,
                                         newLabel.rect.height))
            background.blit(newLabel.image, (0, 0))
            newLabel.image = background
            self.addLabels(newLabel)

    def locationChosen(self, location):
        if location is not self.getParent().currentLocation:
            self.getParent().currentLocation = location
            self.getRoot().fadeMenuChange("mainLocationMenu")


class MapNavigationHandler:
    def __init__(self):
        # Will handle navigating locations buttons and exitting the map
        pass
