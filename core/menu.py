import pygame
from core.inputField import InputField
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
                self.getRoot().exit()
        self.navigationHandler.handleNavigationEvents(events)

    def draw(self, surface, position=(0, 0)):
        self.getRoot().display.draw(surface, position)

    def addButton(self, button):
        self.buttons.append(button)

    def addLabel(self, label):
        self.labels.append(label)

    def addSurface(self, surface):
        self.surfaces.append(surface)

    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState
