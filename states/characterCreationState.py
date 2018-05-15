from core.player import Player
from core.state import State
from menus.classSelectionMenu import ClassSelectionMenu
from menus.raceSelectionMenu import RaceSelectionMenu
from menus.nameChoosingMenu import NameChoosingMenu


class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)
        self.newPlayer = Player()
        self.addMenus(RaceSelectionMenu(self), ClassSelectionMenu(self),
                      NameChoosingMenu(self))
