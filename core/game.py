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
        self.changeMenu("titleMenuState/titleMenu")
        self.running = True

    def loop(self):
        while self.running:
            self.currentState.currentMenu.update()
            self.display.clear()
            self.currentState.currentMenu.render()
            pygame.display.flip()

    def changeMenu(self, menuPath, resetMenu=False):
        splitPath = menuPath.split("/")
        self.currentState = self.getState(splitPath[0])
        self.currentState.changeMenu(splitPath[1])
        if resetMenu:
            self.currentState.resetCurrentMenu()
        self.currentState.currentMenu.updateButtonFocus()

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

    def exit(self):
        self.display.fadeOut(2)
        sys.exit()

    def fadeMenuChange(self, menuPath, resetMenu=False, rate=2):
        self.display.fadeOut(rate)
        self.changeMenu(menuPath, resetMenu)
        self.currentState.currentMenu.render()
        self.display.fadeIn(rate)


class StateNotFoundException(Exception):
    def __init__(self, name):
        super().__init__("Unable to find state: " + name)
