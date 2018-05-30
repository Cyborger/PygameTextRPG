import pygame
from states.titleMenuState import TitleMenuState
from states.characterCreationState import CharacterCreationState
from states.locationState import LocationState
from states.battleState import BattleState
from lib.jsonLoader import JSONLoader
from lib.display import Display
from core.itemManager import ItemManager
from core.locationManager import LocationManager
from core.saveManager import SaveManager
from core.player import Player
from core.console import Console


class Game:
    def __init__(self):
        self.display = Display(700, 700)
        self.itemManager = ItemManager()
        self.locationManager = LocationManager()
        self.saveManager = SaveManager()
        self.states = [TitleMenuState(self), CharacterCreationState(self),
                       LocationState(self), BattleState(self)]
        self.currentState = None
        self.running = True
        self.player = Player()
        self.player.inventory.addItems(self.itemManager.getItem("Sword"))
        self.player.heldWeapon = self.player.inventory.getItems()[0]
        self.console = Console(self)
        self.currentSaveID = "default"
        self.saveManager.createSave(self)

    def start(self):
        self.changeMenu("titleMenuState/titleMenu")
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

    def fadeMenuChange(self, menuPath, duration="normal"):
        timeToFade = {"fast" : 0.5, "normal" : 1.5, "slow" : 2.5}[duration]
        self.display.fadeOut(timeToFade / 2.0)
        self.changeMenu(menuPath)
        self.currentState.currentMenu.render()
        self.display.fadeIn(timeToFade / 2.0)

    def createMessage(self, messages):
        newMessage = Message(messages, self.currentState)
        self.currentState.currentMenu = newMessage

    def exit(self):
        self.display.fadeOut(1.0)

    def enterConsole(self):
        self.console.loop()


class StateNotFoundException(Exception):
    def __init__(self, stateName):
        super().__init__("Unable to find state: " + stateName)
