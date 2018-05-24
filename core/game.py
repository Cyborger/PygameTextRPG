import pygame
from states.titleMenuState import TitleMenuState
from states.characterCreationState import CharacterCreationState
from states.locationState import LocationState
from states.battleState import BattleState
from lib.jsonLoader import JSONLoader
from lib.display import Display
from lib.message import Message
from core.item import Item
from core.player import Player



class Game:
    def __init__(self):
        self.display = Display(700, 700)
        self.states = [TitleMenuState(self), CharacterCreationState(self),
                       LocationState(self), BattleState(self)]
        self.currentState = None
        self.running = True
        self.items = JSONLoader.loadJSONFile("items", Item)
        self.player = Player()
        self.player.inventory.addItem(self.items[0])

    def start(self):
        self.changeMenu("locationState/mainLocationMenu")
        self.loop()

    def loop(self):
        pygame.event.clear()
        while self.running:
            self.currentState.currentMenu.update()
            self.display.clear()
            self.currentState.currentMenu.render()
            pygame.display.flip()
        self.exit()

    def changeMenu(self, menuPath):
        if "/" in menuPath:
            splitPath = menuPath.split("/")
            self.currentState = self.getState(splitPath[0])
            self.currentState.changeMenu(splitPath[1])
        else:
            self.currentState.changeMenu(menuPath)

    def getState(self, stateName):
        for state in self.states:
            if state.name == stateName:
                return state
        raise StateNotFoundException(stateName)

    def getMenu(self, menuPath):
        splitPath = self.splitMenuPath(menuPath)
        return self.getState(splitPath[0]).getMenu(splitPath[1])

    def fadeMenuChange(self, menuPath, duration="normal"):
        timeToFade = {"fast" : 0.75, "normal" : 1.5, "slow" : 2.5}[duration]
        self.display.fadeOut(timeToFade / 2.0)
        self.changeMenu(menuPath)
        self.currentState.currentMenu.render()
        self.display.fadeIn(timeToFade / 2.0)

    def createMessage(self, messages):
        newMessage = Message(messages, self.currentState)
        self.currentState.currentMenu = newMessage

    def exit(self):
        self.display.fadeOut(1.0)


class StateNotFoundException(Exception):
    def __init__(self, stateName):
        super().__init__("Unable to find state: " + stateName)
