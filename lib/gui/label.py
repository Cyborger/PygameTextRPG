import pygame
from lib.gui.surface import Surface


class Label(Surface):
    def __init__(self, text, x=0, y=0, fontSize=24):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        image = self.font.render(self.text, True, (200, 200, 200))
        super().__init__(image, x, y)

    def updateImage(self):
        self.image = self.font.render(self.text, True, (200, 200, 200))
