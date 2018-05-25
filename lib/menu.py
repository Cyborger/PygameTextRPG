import pygame
from lib.gui.inputField import InputField
from lib.menuNavigationHandler import MenuNavigationHandler


class Menu:
    def __init__(self, name, parentState):
        self.name = name
        self.parentState = parentState
        self.navigationHandler = MenuNavigationHandler(self)
        self.buttons = []
        self.labels = []
        self.surfaces = []

    def isNowCurrentMenu(self):
        pass

    def update(self):
        self.handleEvents()

    def render(self):
        for guiElement in self.buttons + self.labels + self.surfaces:
            self.draw(guiElement.image, guiElement.rect)

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.getRoot().running = False
        self.navigationHandler.handleNavigationEvents(events)

    def draw(self, surface, position=(0, 0)):
        self.getRoot().display.draw(surface, position)

    def addButtons(self, *buttons):
        for button in buttons:
            self.buttons.append(button)
        self.navigationHandler.updateButtonFocus()

    def addLabels(self, *labels):
        for label in labels:
            self.labels.append(label)

    def addSurfaces(self, *surfaces):
        for surface in surfaces:
            self.surfaces.append(surface)

    def listElements(self, elements, x, y, spacing=25, align="top"):
        if align == "center":
            totalHeight = 0
            for element in elements:
                totalHeight += element.rect.height
            totalHeight += spacing * (len(elements) - 1)
            y -= totalHeight / 2
        for element in elements:
            element.rect.x = x
            element.rect.y = y
            y += spacing + element.rect.height
        return elements

    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState

    def goBack(self):
        pass
