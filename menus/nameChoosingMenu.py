from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton
from lib.gui.inputField import InputField


class NameChoosingMenu(Menu):
    def __init__(self, parentState):
        super().__init__("nameChoosingMenu", parentState)
        self.addLabels(Label("Enter your name: ", x=20, y=275))
        self.nameInputField = InputField(x=20, y=325)
        self.addButtons(self.nameInputField)
        buttons = [LabelButton("Continue", self.nextMenu),
                   LabelButton("Back", self.goBack)]
        self.buttons.extend(self.listElements(buttons, 20, 600))

    def nextMenu(self):
        if len(self.nameInputField.getContent()) > 0:
            newPlayer = self.getParent().newPlayer
            newPlayer.name = self.nameInputField.getContent()
            self.getRoot().player = newPlayer
            self.getRoot().player.inventory.addItems(self.getRoot().itemManager.getItem("Sword"))
            self.getRoot().player.heldWeapon = self.getRoot().player.inventory.getItems()[0]
            self.getRoot().saveManager.createNewSave(self.getRoot())
            self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                          "slow")

    def goBack(self):
        self.getRoot().fadeMenuChange("classSelectionMenu")
