from core.menu import Menu
from core.gui.labelButton import LabelButton
from core.gui.label import Label
from core.gui.multilineLabel import MultilineLabel


class TitleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("titleMenu", parentState)
        self.addButtons(LabelButton("Begin A New Adventure", 25, 300,
                                   self.newGame),
                        LabelButton("Exit Game", 25, 350, self.exit))
        self.addLabels(MultilineLabel("Something Something Something Something Something Something Something Something", 25, 400))

    def newGame(self):
        newMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(newMenu, fadeRate=1)

    def exit(self):
        self.getRoot().running = False
