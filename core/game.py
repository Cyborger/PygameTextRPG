import pygame
import sys
from core.display import Display
from states.titleMenuState import TitleMenuState
from states.characterCreationState import CharacterCreationState
from states.locationState import LocationState


class Game:
    def __init__(self):
        self.display = Display(700, 700)
        self.states = [TitleMenuState(self), CharacterCreationState(self),
                       LocationState(self)]
        self.currentState = None

    def start(self):
        self.changeMenu("titleMenuState/titleMenu")
        self.loop()

    def loop(self):
        while True:
            self.currentState.currentMenu.update()
            self.display.clear()
            self.currentState.currentMenu.render()
            pygame.display.flip()

    def changeMenu(self, menuPath):
        splitPath = menuPath.split("/")
        self.currentState = self.getState(splitPath[0])
        self.currentState.changeMenu(splitPath[1])

    def getState(self, stateName):
        for state in self.states:
            if state.name == stateName:
                return state
        raise StateNotFoundException(stateName)

    def getMenu(self, menuPath):
        """ menuPath is in the form of stateName/menuName """
        splitPath = menuPath.split("/")
        return self.getState(splitPath[0]).getMenu(splitPath[1])

    def exit(self):
        self.display.fadeOut(2)
        sys.exit()

    def fadeMenuChange(self, menuPath, fadeRate=2.0):
        self.display.fadeOut(fadeRate)
        self.changeMenu(menuPath)
        self.currentState.currentMenu.render()
        self.display.fadeIn(fadeRate)


class StateNotFoundException(Exception):
    def __init__(self, name):
        super().__init__("Unable to find state: " + name)
