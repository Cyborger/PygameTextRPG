import pygame
import os

from states.titleMenuState import TitleMenuState
from states.characterCreationState import CharacterCreationState


class Game:
    def __init__(self):
        pygame.display.set_icon(pygame.image.load("res/icon.png"))
        pygame.display.set_caption("RPG")
        self.displayWidth = 700
        self.displayHeight = 700
        self.display = pygame.display.set_mode((self.displayWidth,
                                                self.displayHeight))

        self.states = [TitleMenuState(self), CharacterCreationState(self)]
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
        self.currentState = self.getState(splitPath[0])
        self.currentState.changeMenu(splitPath[1])

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

    def fadeMenuChange(self, menuPath):
        self.fadeOut(2)
        self.changeMenu(menuPath)
        self.currentState.currentMenu.render()
        self.fadeIn(2)

    def fadeOut(self,fadeRate):
        currentDisplay = self.display.copy()
        fadeSurface = pygame.Surface((self.displayWidth, self.displayHeight))
        for i in range(0, 255, fadeRate):
            fadeSurface.set_alpha(i)
            self.display.blit(currentDisplay, (0, 0))
            self.display.blit(fadeSurface, (0, 0))
            pygame.display.flip()

    def fadeIn(self,fadeRate):
        currentDisplay = self.display.copy()
        fadeSurface = pygame.Surface((self.displayWidth, self.displayHeight))
        for i in range(255, 0, -fadeRate):
            fadeSurface.set_alpha(i)
            self.display.blit(currentDisplay, (0, 0))
            self.display.blit(fadeSurface, (0, 0))
            pygame.display.flip()


class StateNotFoundException(Exception):
    def __init__(self, name):
        super().__init__("Unable to find state: " + name)
