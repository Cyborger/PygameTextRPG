from core.player import Player
from core.state import State
from menus.allocateStatsMenu import AllocateStatsMenu
from menus.raceSelectionMenu import RaceSelectionMenu
from menus.nameChoosingMenu import NameChoosingMenu

class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)
        self.newPlayer = Player()
        self.addMenu(AllocateStatsMenu(self))
        self.addMenu(RaceSelectionMenu(self))
        self.addMenu(NameChoosingMenu(self))
