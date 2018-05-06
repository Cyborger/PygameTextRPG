import pygame


# TODO: Getting buttons?

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
                self.getRoot().exit()
        self.handleKeyEvents(events)
        self.handleMouseEvents(events)

    def draw(self, surface, position=(0, 0)):
        self.getRoot().display.draw(surface, position)

    def addButton(self, button):
        self.buttons.append(button)

    def addLabel(self, label):
        self.labels.append(label)

    def handleKeyEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.buttonSelection = max(self.buttonSelection - 1, 0)
                    self.updateButtonFocus()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.buttonSelection = min(self.buttonSelection + 1,
                                               len(self.buttons) - 1)
                    self.updateButtonFocus()
                elif event.key == pygame.K_RETURN:
                    self.buttons[self.buttonSelection].checkForClick()

    def handleMouseEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.update(event.pos)
                    if button.isHovering(event.pos):
                        self.buttonSelection = self.buttons.index(button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.checkForClick()

    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState

    def updateButtonFocus(self):
        for i in range(len(self.buttons)):
            if i == self.buttonSelection:
                self.buttons[i].forceHover()
            else:
                self.buttons[i].forceUnhover()
