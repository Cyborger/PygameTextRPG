from core.menu import Menu
from core.label import Label
from core.labelButton import LabelButton
from core.inputField import InputField


class NameChoosingMenu(Menu):
    def __init__(self, parentState):
        super().__init__("nameChoosingMenu", parentState)
        self.addLabel(Label("Enter your name: ", 20, 275))
        self.nameInputField = InputField(20, 325)
        self.addButton(self.nameInputField)
        self.addButton(LabelButton("Continue", 20, 600, self.nextMenu))
        self.addButton(LabelButton("Back", 20, 650, self.goBack))

    def nextMenu(self):
        if len(self.nameInputField.getContent()) > 0:
            newPlayer = self.getParent().newPlayer
            newPlayer.name = self.nameInputField.getContent()
            self.getRoot().getState("locationState").player = newPlayer
            self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                          fadeRate = 1)

    def goBack(self):
        newMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(newMenu)
