from core.menu import Menu
from core.labelButton import LabelButton
from core.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)
        self.addButton(LabelButton("Travel", 20, 300, self.placeholder))
        self.addButton(LabelButton("Rest", 20, 350, self.rest))
        self.addButton(LabelButton("Player Stats", 20, 400, self.playerStats))
        self.addLabel(Surface("res/images/forest.png", 425, 200))

    def rest(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu", rate=1)

    def playerStats(self):
        self.getParent().player.printInfo()

    def placeholder(self):
        pass
