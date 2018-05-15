from core.menu import Menu
from core.playerClass import PlayerClass
from core.jsonLoader import JSONLoader
from core.gui.label import Label
from core.gui.labelButton import LabelButton


class ClassSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("classSelectionMenu", parentState)
        self.classes = JSONLoader.loadJSONFile("classes", PlayerClass)
        self.addLabels(Label("Choose a class: ", 10, 20, fontSize=32))
        self.createButtons()

    def createButtons(self):
        x = 40
        y = 70
        ySpacing = 60
        for playerClass in self.classes:
            self.addButtons(LabelButton(playerClass.name, x, y,
                                        self.chooseClass, playerClass))
            y += ySpacing
        self.addButtons(LabelButton("Back", 20, 650, self.goBack))

    def chooseClass(self, playerClass):
        self.getParent().newPlayer.playerClass = playerClass
        self.getRoot().fadeMenuChange("characterCreationState/nameChoosingMenu",
                                      fadeRate=3)
    def goBack(self):
        previousMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(previousMenu, fadeRate=3)
