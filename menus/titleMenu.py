from lib.menu import Menu
from lib.gui.labelButton import LabelButton
from lib.gui.label import Label
from lib.gui.multilineLabel import MultilineLabel


class TitleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("titleMenu", parentState)


    def nowCurrentMenu(self):
        self.buttons[:] = []
        self.addButtons(LabelButton("Begin A New Adventure", self.newGame))
        if len(self.getRoot().saveManager.saves) > 0:
            self.addButtons(LabelButton("Load Character",
                                        self.goToCharacterLoadMenu))
        self.addButtons(LabelButton("Exit Game", self.exit))
        self.listElements(self.buttons, 20, 350, align="center")

    def newGame(self):
        newMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(newMenu, "slow")

    def goToCharacterLoadMenu(self):
        self.getRoot().fadeMenuChange("loadCharacterMenu")

    def exit(self):
        self.getRoot().running = False
