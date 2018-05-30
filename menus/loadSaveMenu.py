from lib.menu import Menu
from lib.gui.labelButton import LabelButton

class LoadSaveMenu(Menu):
    def __init__(self, parentState, menuToReturnTo):
        super().__init__("loadSaveMenu", parentState)
        self.menuToReturnTo = menuToReturnTo

    def nowCurrentMenu(self):
        self.buttons[:] = []
        for save in self.getRoot().saveManager.getSaves():
            self.addButtons(LabelButton(save, self.saveSelected, save))
        self.listElements(self.buttons, 20, 20)
        self.addButtons(LabelButton("Back", self.goBack, x=20, y=600))

    def saveSelected(self, save):
        self.game.saveManager.loadSave(save)
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange(self.menuToReturnTo, "fast")
