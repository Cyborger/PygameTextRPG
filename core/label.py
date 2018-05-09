import pygame
from core.surface import Surface


class Label(Surface):
    def __init__(self, text, x, y, fontSize=24):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        image = self.font.render(self.text, True, (200, 200, 200))
        super().__init__(image, x, y)

    def updateImage(self):
        self.image = self.font.render(self.text, True, (200, 200, 200))
