import pygame

from states.titleMenuState import TitleMenuState

class Game:
    def __init__(self):
        self.windowWidth = 700
        self.windowHeight = 700
        self.display = pygame.display.set_mode((self.windowWidth,
                                                self.windowHeight))
        pygame.display.set_caption("RPG")
        pygame.display.set_icon(pygame.image.load("res/icon.png"))

        self.states = [TitleMenuState(self)]
        self.currentState = None

        self.running = True

    def start(self):
        self.currentState = self.getState("titleMenuState")
        self.loop()

    def loop(self):
        while self.running:
            self.currentState.currentMenu.update()
            self.clearScreen()
            self.currentState.currentMenu.render()
            pygame.display.flip()

    def clearScreen(self, color=(0, 0, 0)):
        self.display.fill(color)

    def changeMenu(self, menuPath):
        splitPath = menuPath.split("/")
        self.currentState = getState(splitPath[0])
        self.currentState.changeMenu(menuPath[1])

    def getState(self, stateName):
        for state in self.states:
            if state.name == stateName:
                return state
        else:
            raise StateNotFoundException(stateName)

    def getMenu(self, menuPath):
        """ menuPath is in the form of stateName/menuName """
        splitPath = menuPath.split("/")
        return self.getState(splitPath[0]).getMenu(splitPath[1])


class StateNotFoundException(Exception):
    def __init__(self, name):
        super().__init__("Unable to find state: " + name)
