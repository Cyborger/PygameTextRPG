from lib.menu import Menu
from lib.gui.multilineLabel import MultilineLabel
from lib.gui.labelButton import LabelButton

class RaceConfirmationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceConfirmationMenu", parentState)
        self.addButtons(LabelButton("Confirm Choice", self.nextMenu),
                        LabelButton("Back", self.goBack))
        self.listElements(self.buttons, 20, 600)

    def isNowCurrentMenu(self):
        self.labels[:] = []
        description = self.getParent().newPlayer.race.description
        self.addLabels(MultilineLabel(description, x=40, y=40, maxWidth=600))

    def nextMenu(self):
        self.getRoot().fadeMenuChange("classSelectionMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("raceSelectionMenu", "fast")
