import pygame
from core.button import Button
from core.label import Label

class InputField(Button):
    def __init__(self, x, y, parentMenu, maxLength=20, fontSize = 24):
        self.parentMenu = parentMenu
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.borderWidth = 2
        self.xMargin = 3
        self.yMargin = 6
        self.boxImage = self.createBoxImage(maxLength)
        self.inputLabel = Label("", self.borderWidth + self.xMargin,
                                self.borderWidth + self.yMargin)
        super().__init__(self.boxImage, x, y, self.getInput)
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

    def getInput(self):
        gettingInput = True
        while gettingInput:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gettingInput = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gettingInput = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.inputLabel.text = self.inputLabel.text[:-1]
                        self.renderInput()
                    else:
                        self.inputLabel.text += event.unicode
                        self.renderInput()
            self.parentMenu.render()
            pygame.display.flip()

    def renderInput(self):
        self.image = self.boxImage.copy()
        self.inputLabel.updateImage()
        self.image.blit(self.inputLabel.image, self.inputLabel.rect)
