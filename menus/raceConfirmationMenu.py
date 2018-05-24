from lib.menu import Menu
from lib.gui.multilineLabel import MultilineLabel
from lib.gui.labelButton import LabelButton

class RaceConfirmationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceConfirmationMenu", parentState)
        self.addButtons(LabelButton("Confirm Choice", 20, 600, self.nextMenu),
                        LabelButton("Back", 20, 650, self.goBack))

    def isNowCurrentMenu(self):
        self.labels[:] = []
        description = self.getParent().newPlayer.race.description
        self.addLabels(MultilineLabel(description, 40, 40, maxWidth=600))

    def nextMenu(self):
        self.getRoot().fadeMenuChange("classSelectionMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("raceSelectionMenu", "fast")
