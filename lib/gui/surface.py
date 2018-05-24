import pygame


class Surface:
    def __init__(self, image, x, y):
        self.image = self.loadImage(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loadImage(self, image):
        if isinstance(image, str):
            return pygame.image.load(image)
        elif isinstance(image, pygame.Surface):
            return image
        else:
            raise InvalidSurfaceException(image)


class InvalidSurfaceException(Exception):
    def __init__(self, attemptedSurface):
        message = ("Failure to create surface image using %s please use a " +
            "valid filepath or a pygame surface" % attemptedSurface)
        super().__init__(message)
