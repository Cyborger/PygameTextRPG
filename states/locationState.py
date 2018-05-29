import random
from menus.mainLocationMenu import MainLocationMenu
from menus.travelMenu import TravelMenu
from menus.playerInfoMenu import PlayerInfoMenu
from menus.inventoryMenu import InventoryMenu
from lib.jsonLoader import JSONLoader
from lib.state import State
from core.location import Location
from core.player import Player


class LocationState(State):
    def __init__(self, game):
        super().__init__("locationState", game)
        self.currentLocation = self.getRoot().\
                locationManager.getLocation("camp")
        self.addMenus(MainLocationMenu(self), TravelMenu(self),
                      PlayerInfoMenu(self),
                      InventoryMenu(self, "mainLocationMenu"))

    def changeLocation(self, location):
        self.currentLocation = location
        if self.currentLocation.hasEnemies():
            self.lookForEnemies()
        else:
            self.getRoot().fadeMenuChange("mainLocationMenu")

    def lookForEnemies(self):
        roll = random.randint(1, 2)
        if roll == 2:
            location = self.currentLocation
            self.getRoot().getState("battleState").newBattle(location)
        else:
            self.getRoot().fadeMenuChange("mainLocationMenu")
