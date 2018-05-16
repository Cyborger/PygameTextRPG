import pygame


# TODO: Make fading rate universal across computers of different speeds

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
        self.fade(interval, fadingIn = True)

    def fadeOut(self, interval):
        self.fade(interval, fadingIn = False)

    # 0 = transparent
    # 255 = opaque
    def fade(self, interval, fadingIn = True):
        """ fadeType is either 'out' or 'in' """
        intervalMS = interval * 1000.0
        print("Must take %sms to finish" % intervalMS)
        fadingSurface = pygame.Surface((self.width, self.height))
        currentDisplay = self.display.copy()
        startTime = pygame.time.get_ticks()
        print("Current time: %s" % startTime )
        timePassed = 0.0
        while timePassed < intervalMS:
            progress = timePassed / intervalMS
            alpha = int(progress * 255.0)
            if fadingIn:
                alpha = 255 - alpha
            fadingSurface.set_alpha(alpha)
            self.draw(currentDisplay)
            self.draw(fadingSurface)
            pygame.display.flip()
            currentTime = pygame.time.get_ticks()
            timePassed = (currentTime - startTime)
            print("Current time is: %s" % currentTime)
            print("Start time is: %s" % startTime)
            print("So %s have passed" % timePassed)
