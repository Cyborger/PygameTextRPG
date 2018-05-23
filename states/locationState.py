import random
from core.jsonLoader import JSONLoader
from core.location import Location
from core.state import State
from core.player import Player
from menus.mainLocationMenu import MainLocationMenu
from menus.travelMenu import TravelMenu
from menus.playerInfoMenu import PlayerInfoMenu


class LocationState(State):
    def __init__(self, game):
        super().__init__("locationState", game)
        self.locations = JSONLoader.loadJSONFile("locations", Location)
        self.currentLocation = self.locations[0]
        self.addMenus(MainLocationMenu(self), TravelMenu(self),
                      PlayerInfoMenu(self))

    def changeLocation(self, location):
        # Figure out if battle or not
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

    def getLocation(self, locationName):
        for location in self.locations:
            if location.name == locationName:
                return location


class LocationNotFoundException(Exception):
    def __init__(self, locationName):
        super().__init__("Unable to find location: " + locationName)
