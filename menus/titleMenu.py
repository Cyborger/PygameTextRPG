from core.menu import Menu
from core.labelButton import LabelButton
from core.label import Label

class TitleMenu(Menu):
    def __init__(self, game):
        super().__init__("titleMenu", game)
        self.addButton(LabelButton("Begin A New Adventure", 25, 300, self.newGame))
        self.addButton(LabelButton("Exit Game", 25, 350, self.exit))

    def newGame(self):
        self.getRoot().fadeMenuChange("characterCreationState/allocateStatsMenu")

    def exit(self):
        self.getRoot().running = False
