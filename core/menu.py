import pygame
from core.gui.inputField import InputField
from core.menuNavigationHandler import MenuNavigationHandler


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

    def addLabels(self, *labels):
        for label in labels:
            self.labels.append(label)

    def addSurface(self, *surfaces):
        for surface in surfaces:
            self.surfaces.append(surface)

    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState
