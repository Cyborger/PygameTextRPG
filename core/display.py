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

    def clear(self, color = (0, 0, 0)):
        self.display.fill(color)

    def fadeIn(self, fadeRate):
        fadingSurface = pygame.Surface((self.width, self.height))
        currentDisplay = self.display.copy()
        timeBetween = (fadeRate / 1000.0) / 255.0
        for i in range(255, 0, int(-fadeRate)):
            fadingSurface.set_alpha(i)
            self.display.blit(currentDisplay, (0, 0))
            self.display.blit(fadingSurface, (0, 0))
            pygame.display.flip()
            pygame.time.wait(int(timeBetween))

    def fadeOut(self, fadeRate):
        fadingSurface = pygame.Surface((self.width, self.height))
        currentDisplay = self.display.copy()
        timeBetween = (fadeRate / 1000.0) / 255.0
        for i in range(0, 255, int(fadeRate)):
            fadingSurface.set_alpha(i)
            self.draw(currentDisplay)
            self.draw(fadingSurface)
            pygame.display.flip()
            pygame.time.wait(int(timeBetween))

    def draw(self, image, position = (0, 0)):
        self.display.blit(image, position)
