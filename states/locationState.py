from core.jsonLoader import JSONLoader
from core.location import Location
from core.state import State
from core.player import Player
from menus.mainLocationMenu import MainLocationMenu
from menus.travelMenu import TravelMenu


class LocationState(State):
    def __init__(self, game):
        super().__init__("locationState", game)
        self.locations = JSONLoader.loadJSONFile("locations", Location)
        self.currentLocation = self.locations[0]
        self.player = Player()  # Default player, if skipping character creation
        self.addMenus(MainLocationMenu(self), TravelMenu(self))
