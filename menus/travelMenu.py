import pygame
from core.menu import Menu
from core.gui.surface import Surface
from core.gui.imageButton import ImageButton
from core.gui.label import Label
from core.gui.labelButton import LabelButton
from core.menuNavigationHandler import MenuNavigationHandler


class TravelMenu(Menu):
    def __init__(self, parentState):
        super().__init__("travelMenu", parentState)
        self.navigationHandler = MapNavigationHandler(self)

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
        self.surfaces[:] = []
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
        self.buttons[:] = []
        buttonImage = pygame.image.load("res/buttons/mapDefault.png")
        buttonImageCurrent = pygame.image.load("res/buttons/mapCurrent.png")
        buttonImageHovered = pygame.image.load("res/buttons/mapHovered.png")

        for location in self.getParent().locations:
            x, y = location.mapLocation[0] - 16, location.mapLocation[1] - 16
            if location == self.getParent().currentLocation:
                # Can't select because it is the current location
                button = ImageButton(buttonImageCurrent, buttonImageCurrent,
                    x, y, self.locationChosen, location)
                self.addButtons(button)
            elif self.getParent().currentLocation.locationIsAdjacent(location):
                # Can select because it is adjacent to current
                button = ImageButton(buttonImage, buttonImageHovered, x, y,
                    self.locationChosen, location)
                self.addButtons(button)
            else:
                # Can't select because not adjacent
                button = ImageButton(buttonImage, buttonImage, x, y,
                    self.locationChosen, location)
                self.addButtons(button)
        self.addButtons(LabelButton("Back", 20, 650, self.goBack))

    def createLabels(self):
        self.labels[:] = []
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
        currentLocation = self.getParent().currentLocation
        isAdjacent = currentLocation.locationIsAdjacent(location)
        if (location is not currentLocation) and isAdjacent:
            self.getParent().changeLocation(location)

    def goBack(self):
        self.getRoot().fadeMenuChange("mainLocationMenu")


class MapNavigationHandler(MenuNavigationHandler):
    def __init__(self, menu):
        super().__init__(menu)

    def resetSelection(self):
        self.currentLocation = self.menu.getParent().currentLocation
        self.locationSelected(self.currentLocation.name)
        self.updateButtonFocus()

    def handleMenuNavigationEvent(self, event):
        if event.key == pygame.K_RETURN:
            self.selectedButton.checkForClick()
        elif event.key == pygame.K_ESCAPE:
            self.menu.goBack()
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.selectLocation("North")
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.selectLocation("East")
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.selectLocation("South")
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.selectLocation("West")


    def selectLocation(self, direction):
        if direction in self.currentLocation.connectedLocations:
            location = self.currentLocation.connectedLocations[direction]
            self.locationSelected(location)
        else:
            self.resetSelection()

    def locationSelected(self, locationName):
        location = self.menu.getParent().getLocation(locationName)
        self.selectedButton = self.getLocationButton(location)
        self.updateButtonFocus()

    def getLocationButton(self, location):
        for button in self.menu.buttons:
            if button.funcArgs[0] == location:
                return button
