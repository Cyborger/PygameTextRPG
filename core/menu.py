import pygame
from core.inputField import InputField


class Menu:
    def __init__(self, name, parentState):
        self.name = name
        self.parentState = parentState
        self.buttons = []
        self.labels = []
        self.currentTextField = None
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
        self.handleMouseEvents(events)
        if self.currentTextField is None:
            self.handleButtonNavigationEvents(events)
        else:
            self.handleInputEnteringEvents(events)


    def draw(self, surface, position=(0, 0)):
        self.getRoot().display.draw(surface, position)

    def addButton(self, button):
        self.buttons.append(button)

    def addLabel(self, label):
        self.labels.append(label)

    def handleButtonNavigationEvents(self, events):
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
                    selectedButton = self.buttons[self.buttonSelection]
                    selectedButton.checkForClick()
                    if isinstance(selectedButton, InputField):
                        self.currentTextField = selectedButton

    def handleInputEnteringEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    self.currentTextField.unselected()
                    self.currentTextField = None
                elif event.key == pygame.K_BACKSPACE:
                    self.currentTextField.backspace()
                else:
                    self.currentTextField.addInput(event.unicode)

    def handleMouseEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.update(event.pos)
                    if button.isHovering(event.pos):
                        self.buttonSelection = self.buttons.index(button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.currentTextField is not None:
                    self.currentTextField.unselected()
                    self.currentTextField = None
                for button in self.buttons:
                    if button.hovered:
                        button.click(*button.funcArgs)
                        if isinstance(button, InputField):
                            self.currentTextField = button
                            self.currentTextField.selected()


    def getRoot(self):
        return self.parentState.getRoot()

    def getParent(self):
        return self.parentState

    def updateButtonFocus(self):
        for i in range(len(self.buttons)):
            if i == self.buttonSelection:
                self.buttons[i].forceHover()
                if isinstance(self.buttons[i], InputField):
                    self.currentTextField = self.buttons[i]
                    self.buttons[i].selected()
            else:
                self.buttons[i].forceUnhover()
