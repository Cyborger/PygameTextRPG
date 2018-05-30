from lib.menu import Menu
from lib.gui.labelButton import LabelButton

class LoadCharacterMenu(Menu):
    def __init__(self, parentState, menuToReturnTo):
        super().__init__("loadCharacterMenu", parentState)
        self.menuToReturnTo = menuToReturnTo

    def nowCurrentMenu(self):
        self.buttons[:] = []
        for save in self.getRoot().saveManager.saves:
            self.addButtons(LabelButton(save.getTitle(),
                                        self.saveSelected, save, fontSize=16))
        self.listElements(self.buttons, 20, 20)
        self.addButtons(LabelButton("Back", self.goBack, x=20, y=600))

    def saveSelected(self, save):
        save.load(self.getRoot())
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange(self.menuToReturnTo, "fast")
