import pygame


class Menu:
    def __init__(self, name, parentState):
        self.name = name
        self.parentState = parentState
        self.buttons = []
        self.labels = []

    def update(self):
        self.handleEvents()

    def render(self):
        for guiElement in self.buttons + self.labels:
            self.draw(guiElement.image, guiElement.rect)

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.getRoot().running = False
        self.handleButtonEvents(events)

    def draw(self, surface, position=(0, 0)):
        self.getRoot().display.blit(surface, position)

    def addButton(self, button):
        self.buttons.append(button)

    def addLabel(self, label):
        self.labels.append(label)

    def handleButtonEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.update(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.checkForClick()

    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState
