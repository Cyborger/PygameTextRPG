import pygame


class Label:
    def __init__(self, text, x, y, fontSize=24):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        self.image = self.font.render(self.text, True, (200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
