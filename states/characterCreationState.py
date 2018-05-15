from core.player import Player
from core.state import State
from menus.classSelectionMenu import ClassSelectionMenu
from menus.classConfirmationMenu import ClassConfirmationMenu
from menus.raceSelectionMenu import RaceSelectionMenu
from menus.raceConfirmationMenu import RaceConfirmationMenu
from menus.nameChoosingMenu import NameChoosingMenu


class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)
        self.newPlayer = Player()
        self.addMenus(RaceSelectionMenu(self), RaceConfirmationMenu(self),
                      ClassSelectionMenu(self), ClassConfirmationMenu(self),
                      NameChoosingMenu(self))
