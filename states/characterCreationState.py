from core.state import State
from menus.allocateStatsMenu import AllocateStatsMenu

class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)

        self.playerName = ""
        self.playerStrength = 10
        self.playerDexterity = 10
        self.playerIntelligence = 10
        self.playerLuck = 10

        #self.addMenu(AllocateStatsMenu(self))
