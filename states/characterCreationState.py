from menus.classSelectionMenu import ClassSelectionMenu
from menus.classConfirmationMenu import ClassConfirmationMenu
from menus.raceSelectionMenu import RaceSelectionMenu
from menus.raceConfirmationMenu import RaceConfirmationMenu
from menus.nameChoosingMenu import NameChoosingMenu
from lib.state import State
from core.player import Player


class CharacterCreationState(State):
    def __init__(self, game):
        super().__init__("characterCreationState", game)
        self.newPlayer = Player()
        self.addMenus(RaceSelectionMenu(self), RaceConfirmationMenu(self),
                      ClassSelectionMenu(self), ClassConfirmationMenu(self),
                      NameChoosingMenu(self))
