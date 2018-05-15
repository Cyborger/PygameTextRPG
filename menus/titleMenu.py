from core.menu import Menu
from core.gui.labelButton import LabelButton
from core.gui.label import Label


class TitleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("titleMenu", parentState)
        self.addButton(LabelButton("Begin A New Adventure", 25, 300,
                                   self.newGame))
        self.addButton(LabelButton("Exit Game", 25, 350, self.exit))

    def newGame(self):
        newMenu = "characterCreationState/allocateStatsMenu"
        self.getRoot().fadeMenuChange(newMenu, fadeRate=1)

    def exit(self):
        self.getRoot().running = False
