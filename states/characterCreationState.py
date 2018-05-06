from core.player import Player
from core.state import State
from menus.allocateStatsMenu import AllocateStatsMenu

class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)
        self.newPlayer = Player()
        self.addMenu(AllocateStatsMenu(self))
