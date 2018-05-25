import pygame
from lib.gui.surface import Surface


class MultilineLabel(Surface):
    def __init__(self, text, x=0, y=0, maxWidth=400, fontSize=24):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.maxWidth = maxWidth
        super().__init__(self.renderImage(), x, y)

    def renderImage(self):
        lineWidth = self.maxWidth
        lineHeight = self.font.size(" ")[1]
        lines = self.getLines(self.text)
        imageHeight =  lineHeight * len(lines)
        image = pygame.Surface((lineWidth, imageHeight))
        y = 0
        for line in lines:
            lineImage = self.font.render(line, True, (200, 200, 200))
            image.blit(lineImage, (0, y))
            y += lineHeight
        image.set_colorkey((0, 0, 0))
        image = image.subsurface(image.get_bounding_rect())
        return image


    def getLines(self, text):
        lines = []
        lastSpace = 0
        for i in range(len(text)):
            if self.font.size(text[:i + 1])[0] > self.maxWidth:
                lines.append(text[0:lastSpace])
                remainingText = text[lastSpace+1:]
                if len(remainingText) > 0:
                    lines.extend(self.getLines(remainingText))
                return lines
            if text[i] == " ":
                lastSpace = i
        lines.append(text)
        return lines
