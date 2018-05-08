import pygame
from core.button import Button
from core.label import Label

class InputField(Button):
    def __init__(self, x, y, maxLength=20, fontSize = 24):
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.borderWidth = 2
        self.xMargin = 3
        self.yMargin = 6
        self.maxLength = maxLength

        self.boxImage = self.createBoxImage(maxLength)
        self.inputLabel = Label("", self.borderWidth + self.xMargin,
                                self.borderWidth + self.yMargin)
        super().__init__(self.boxImage, x, y, self.selected)

        self.promptImage = pygame.Surface((2, self.font.size(" ")[1]))
        self.promptImage.fill((200, 200, 200))
        self.showPrompt = False
        self.renderInput()

    def createBoxImage(self, textLength):
        fieldSize = self.font.size(" " * textLength)
        backgroundWidth = fieldSize[0] + self.borderWidth * 2 + self.xMargin * 2
        backgroundHeight = fieldSize[1] + self.borderWidth * 2 + self.yMargin * 2
        background = pygame.Surface((backgroundWidth, backgroundHeight))
        background.fill((255, 255, 255))
        foreground = pygame.Surface((fieldSize[0] + self.xMargin * 2,
                                     fieldSize[1] + self.yMargin * 2))
        background.blit(foreground, (self.borderWidth, self.borderWidth))
        return background

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
        promptX = self.inputLabel.rect.x + self.font.size(self.inputLabel.text)[0]
        promptY = self.inputLabel.rect.y
        self.image.blit(self.promptImage, (promptX, promptY))

    def selected(self):
        self.showPrompt = True
        self.renderInput()

    def unselected(self):
        self.showPrompt = False
        self.renderInput()
