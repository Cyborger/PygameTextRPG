from core.menu import Menu
from core.label import Label
from core.labelButton import LabelButton
from core.inputField import InputField


class NameChoosingMenu(Menu):
    def __init__(self, parentState):
        super().__init__("nameChoosingMenu", parentState)
        self.addLabel(Label("Enter your name: ", 20, 20))
        self.addButton(InputField(20, 120, self))
        self.addButton(LabelButton("Back", 20, 650, self.goBack))

    def goBack(self):
        newMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(newMenu)
