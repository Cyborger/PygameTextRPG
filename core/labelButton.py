import pygame
from core.button import Button


class LabelButton(Button):
    def __init__(self, text, x, y, func, *funcArgs):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf", 24)
        image = self.font.render(self.text, True, (200, 200, 200))
        super().__init__(image, x, y, func, *funcArgs)

    def hover(self):
        self.image = self.font.render(">" + self.text, True, (255, 255, 255))

    def unhover(self):
        self.image = self.font.render(self.text, True, (200, 200, 200))
