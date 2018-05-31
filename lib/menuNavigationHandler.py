import pygame
from lib.gui.inputField import InputField


class MenuNavigationHandler:
    def __init__(self, menu):
        self.menu = menu
        self.selectedButton = None
        self.currentTextField = None

    def resetSelection(self):
        self.selectedButton = self.menu.buttons[0]
        if not isinstance(self.menu.buttons[0], InputField):
            for button in self.menu.buttons:
                if button.isHovering(pygame.mouse.get_pos()):
                    button.hovered = True
        self.updateButtonFocus()

    def handleNavigationEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.updateButtons(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handleMouseClick()
            elif event.type == pygame.KEYDOWN:
                self.handleKeyPressEvents(event)

    def handleKeyPressEvents(self, event):
        if self.currentTextField is None:
            self.handleMenuNavigationEvent(event)
        else:
            self.handleTextFieldInputEvent(event)

    def updateButtons(self, mousePosition):
        for button in self.menu.buttons:
            button.update(mousePosition)
            if button.hovered:
                self.selectedButton = button

    def handleMouseClick(self):
        self.currentTextField = None
        for button in self.menu.buttons:
            if isinstance(button, InputField):
                button.checkForClick(self)
            else:
                button.checkForClick()
        pygame.event.clear()

    def handleTextFieldInputEvent(self, event):
        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
            self.currentTextField.unselected()
            self.currentTextField = None
        elif event.key == pygame.K_BACKSPACE:
            self.currentTextField.backspace()
        else:
            self.currentTextField.addInput(event.unicode)

    def handleMenuNavigationEvent(self, event):
        if event.key == pygame.K_ESCAPE:
            self.menu.goBack()
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            currentIndex = self.menu.buttons.index(self.selectedButton)
            nextButton = max(currentIndex - 1, 0)
            self.selectedButton = self.menu.buttons[nextButton]
            self.updateButtonFocus()
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            currentIndex = self.menu.buttons.index(self.selectedButton)
            previousButton = min(currentIndex + 1, len(self.menu.buttons) - 1)
            self.selectedButton = self.menu.buttons[previousButton]
            self.updateButtonFocus()
        elif event.key == pygame.K_RETURN:
            if isinstance(self.selectedButton, InputField):
                self.selectedButton.checkForClick(self)
            else:
                self.selectedButton.checkForClick()
                pygame.event.clear()

    def updateButtonFocus(self):
        for button in self.menu.buttons:
            if button == self.selectedButton:
                self.selectedButton.hover()
                if isinstance(self.selectedButton, InputField):
                    self.currentTextField = button
                    button.selected()
            else:
                button.unhover()
