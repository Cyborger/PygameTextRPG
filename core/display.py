import pygame


class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = None
        self.initialize()

    def initialize(self):
        pygame.display.set_icon(pygame.image.load("res/images/icon.png"))
        pygame.display.set_caption("RPG")
        self.display = pygame.display.set_mode((self.width, self.height))

    def draw(self, image, position = (0, 0)):
        self.display.blit(image, position)

    def clear(self, color = (0, 0, 0)):
        self.display.fill(color)

    def fadeIn(self, interval):
        self.fade(interval, invert=True)

    def fadeOut(self, interval):
        self.fade(interval, invert=False)

    def fade(self, interval, invert=True):
        fadingSurface = pygame.Surface((self.width, self.height))
        currentDisplay = self.display.copy()
        startTime = pygame.time.get_ticks()
        intervalMS = interval * 1000.0
        timePassed = 0.0
        while timePassed < intervalMS:
            alpha = int(255 * timePassed / intervalMS)
            if invert:
                fadingSurface.set_alpha(255 - alpha)  # Invert alpha
            else:
                fadingSurface.set_alpha(alpha)
            self.draw(currentDisplay)
            self.draw(fadingSurface)
            pygame.display.flip()
            timePassed = pygame.time.get_ticks() - startTime
