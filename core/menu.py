import pygame


class Menu:
    def __init__(self, name, parentState):
        self.name = name
        self.parentState = parentState
        self.buttons = []
        self.labels = []
        self.buttonSelection = 0

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.selectAboveButton()
                elif event.key == pygame.K_s:
                    self.selectBelowButton()
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

    def selectAboveButton(self):
        self.buttonSelection = max(self.buttonSelection - 1, 0)
        self.focusSelectedButton()

    def selectBelowButton(self):
        self.buttonSelection = min(self.buttonSelection + 1, len(self.buttons))
        self.focusSelectedButton()

    def focusSelectedButton(self):
        for i in range(len(self.buttons)):
            if i == self.buttonSelection:
                self.buttons[i].hover()
            else:
                self.buttons[i].unhover()
