from core.jsonLoader import JSONLoader
from core.state import State
from core.player import Player
from menus.mainLocationMenu import MainLocationMenu


class LocationState(State):
    def __init__(self, game):
        super().__init__("locationState", game)
        # self.locations = JSONLoader.loadJSONFile()
        self.player = Player()  # Default player, if skipping character creation
        self.currentLocation = None
        self.addMenu(MainLocationMenu(self))
