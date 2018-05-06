import pygame

from core.button import Button

class ImageButton(Button):
    def __init__(self, unhoveredImage, hoveredImage, x , y, func, *funcArgs):
        super().__init__(unhoveredImage, x, y, func, *funcArgs)
        self.unhoveredImage = unhoveredImage
        self.hoveredImage = hoveredImage

    def hover(self):
        self.image = self.hoveredImage

    def unhover(self):
        self.image = self.unhoveredImage

    @classmethod
    def fromFilePaths(cls, unhoveredImagePath, hoveredImagePath, x, y, func):
        return cls(pygame.image.load(unhoveredImagePath),
                   pygame.image.load(hoveredImagePath), x, y, func)
