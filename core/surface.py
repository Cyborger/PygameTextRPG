import pygame


#TODO: Consider incorperating into buttons

class Surface:
    def __init__(self, filepath, x, y):
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
