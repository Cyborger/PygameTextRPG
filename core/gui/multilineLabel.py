import pygame
from core.gui.surface import Surface


class MultilineLabel(Surface):
    def __init__(self, text, x, y, maxLength=20, fontSize=24):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.maxLength = maxLength
        super().__init__(self.renderImage(), x, y)

    def renderImage(self):
        lineWidth = self.font.size(" " * self.maxLength)[0]
        lineHeight = self.font.size(" ")[1]
        lines = self.getLines(self.text)
        imageHeight =  lineHeight * len(lines)
        image = pygame.Surface((lineWidth, imageHeight))
        y = 0
        for line in lines:
            lineImage = self.font.render(line, True, (200, 200, 200))
            image.blit(lineImage, (0, y))
            y += lineHeight
        return image


    def getLines(self, text):
        lines = []
        lastSpace = 0
        for i in range(len(text)):
            if i > self.maxLength:
                lines.append(text[0:lastSpace])
                remainingText = text[lastSpace+1:]
                if len(remainingText) > 0:
                    lines.extend(self.getLines(remainingText))
                return lines
            if text[i] == " ":
                lastSpace = i
        lines.append(text)
        return lines
