from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton
from lib.gui.inputField import InputField


class NameChoosingMenu(Menu):
    def __init__(self, parentState):
        super().__init__("nameChoosingMenu", parentState)
        self.addLabels(Label("Enter your name: ", 20, 275))
        self.nameInputField = InputField(20, 325)
        self.addButtons(self.nameInputField,
                        LabelButton("Continue", 20, 600, self.nextMenu),
                        LabelButton("Back", 20, 650, self.goBack))

    def nextMenu(self):
        if len(self.nameInputField.getContent()) > 0:
            newPlayer = self.getParent().newPlayer
            newPlayer.name = self.nameInputField.getContent()
            self.getRoot().player = newPlayer
            self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                          "slow")

    def goBack(self):
        self.getRoot().fadeMenuChange("classSelectionMenu")
