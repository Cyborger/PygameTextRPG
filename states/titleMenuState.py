from core.state import State
from menus.titleMenu import TitleMenu


class TitleMenuState(State):
    def __init__(self, game):
        super().__init__("titleMenuState", game)
        self.addMenus(TitleMenu(self))
