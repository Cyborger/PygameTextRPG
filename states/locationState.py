from core.state import State
from menus.mainLocationMenu import MainLocationMenu


class LocationState(State):
    def __init__(self, game):
        super().__init__("locationState", game)
        self.addMenu(MainLocationMenu(self))
