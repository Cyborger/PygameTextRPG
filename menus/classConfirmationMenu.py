from core.menu import Menu
from core.gui.multilineLabel import MultilineLabel
from core.gui.labelButton import LabelButton


class ClassConfirmationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("classConfirmationMenu", parentState)
        self.classDescription = None
        self.addButtons(LabelButton("Confirm Choice", 20, 600, self.nextMenu),
                        LabelButton("Back", 20, 650, self.goBack))

    def isNowCurrentMenu(self):
        self.labels[:] = []
        description = self.getParent().newPlayer.playerClass.description
        self.addLabels(MultilineLabel(description, 40, 40, maxWidth=600,
                                     fontSize=24))

    def nextMenu(self):
        nextMenu = "characterCreationState/nameChoosingMenu"
        self.getRoot().fadeMenuChange(nextMenu, fadeRate=3)

    def goBack(self):
        previousMenu = "characterCreationState/classSelectionMenu"
        self.getRoot().fadeMenuChange(previousMenu, fadeRate=3)
