import pygame


class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hovered = False

    def update(self, mousePosition):
        if self.isHovering(mousePosition) and not self.hovered:
            self.hover()
            self.hovered = True
        elif not self.isHovering(mousePosition) and self.hovered:
            self.unhover()
            self.hovered = False

    def isHovering(self, mousePosition):
        if self.rect.collidepoint(mousePosition):
            return True
        return False

    def checkForClick(self):
        if self.hovered:
            self.click()

    def hover(self):
        pass

    def unhover(self):
        pass

    def click(self):
        pass
