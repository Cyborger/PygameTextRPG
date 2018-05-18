import pygame
from core.menu import Menu
from core.gui.imageButton import ImageButton


class TravelMenu(Menu):
    def __init__(self, parentState):
        super().__init__("travelMenu", parentState)
        self.createBackground()
        self.createButtons()

    def createBackground(self):
        # Create lines between locations
        pass

    def createButtons(self):
        # Create all the location buttons and the back button
        buttonImage = pygame.image.load("res/images/mapButtonDefault.png")
        buttonImageHovered = pygame.image.load("res/images/" +
                                                 "mapButtonHovered.png")

        for location in self.getParent().locations:
            x, y = location.mapLocation
            self.addButtons(ImageButton(buttonImage, buttonImageHovered,
                                        x, y, self.locationChosen, location))


    def locationChosen(self, location):
        print("You will travel to: " + location.name)

class MapNavigationHandler:
    def __init__(self):
        # Will handle navigating locations buttons and exitting the map
        pass
