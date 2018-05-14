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
        self._fade(255.0, 0.0, -fadeRate)

    def fadeOut(self, fadeRate):
        self._fade(0.0, 255.0, fadeRate)

    def _fade(self, startAlpha, endAlpha, fadeRate):
        fadingSurface = pygame.Surface((self.width, self.height))
        currentDisplay = self.display.copy()
        timeBetween = (abs(fadeRate) / 1000.0) / 255.0
        for i in self._getFadeIncrements(startAlpha, endAlpha, fadeRate):
            lastTime = pygame.time.get_ticks()
            fadingSurface.set_alpha(int(i))
            self.draw(currentDisplay)
            self.draw(fadingSurface)
            pygame.display.flip()
            timeToRender = pygame.time.get_ticks() - lastTime
            pygame.time.delay(int(timeBetween - timeToRender))

    def _getFadeIncrements(self, start, finish, increment):
        values = []
        current = start
        if start > finish:
            while current > finish:
                values.append(current)
                current += increment
        elif start < finish:
            while current < finish:
                values.append(current)
                current += increment
        return values

    def draw(self, image, position = (0, 0)):
        self.display.blit(image, position)
