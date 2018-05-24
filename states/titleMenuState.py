from menus.titleMenu import TitleMenu
from lib.state import State


class TitleMenuState(State):
    def __init__(self, game):
        super().__init__("titleMenuState", game)
        self.addMenus(TitleMenu(self))
