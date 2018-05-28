import pygame
from lib.gui.button import Button
from lib.gui.label import Label


class InputField(Button):
    def __init__(self, x=0, y=0, maxLength=20, fontSize = 24):
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.borderWidth = 2
        self.xMargin = 3
        self.yMargin = 6
        self.maxLength = maxLength

        self.boxImage = self.createBoxImage(maxLength)
        self.inputLabel = Label("", self.borderWidth + self.xMargin,
                                self.borderWidth + self.yMargin)
        super().__init__(self.boxImage, self.selected, x=x, y=y)

        self.promptImage = pygame.Surface((2, self.font.size(" ")[1]))
        self.promptImage.fill((200, 200, 200))
        self.showPrompt = False
        self.renderInput()

    def createBoxImage(self, textLength):
        fieldSize = self.font.size(" " * textLength)
        xSpacing = self.borderWidth * 2 + self.xMargin * 2
        backgroundWidth = fieldSize[0] + xSpacing
        ySpacing = self.borderWidth * 2 + self.yMargin * 2
        backgroundHeight = fieldSize[1] + ySpacing

        image = pygame.Surface((backgroundWidth, backgroundHeight))
        image.fill((255, 255, 255))
        foreground = pygame.Surface((fieldSize[0] + self.xMargin * 2,
                                     fieldSize[1] + self.yMargin * 2))
        image.blit(foreground, (self.borderWidth, self.borderWidth))
        return image

    def addInput(self, char):
        if len(self.inputLabel.text) < self.maxLength:
            self.inputLabel.text += char
            self.renderInput()

    def backspace(self):
        self.inputLabel.text = self.inputLabel.text[:-1]
        self.renderInput()

    def renderInput(self):
        self.image = self.boxImage.copy()
        self.inputLabel.updateImage()
        self.image.blit(self.inputLabel.image, self.inputLabel.rect)
        if self.showPrompt:
            self.renderPrompt()

    def renderPrompt(self):
        promptX = (self.inputLabel.rect.x +
            self.font.size(self.inputLabel.text)[0])
        promptY = self.inputLabel.rect.y
        self.image.blit(self.promptImage, (promptX, promptY))

    def checkForClick(self, menuNavigationHandler):
        if self.hovered:
            menuNavigationHandler.currentTextField = self
            self.selected()
        else:
            self.unselected()

    def selected(self):
        self.showPrompt = True
        self.renderInput()

    def unselected(self):
        self.showPrompt = False
        self.renderInput()

    def getContent(self):
        return self.inputLabel.text
