from lib.menu import Menu
from lib.jsonLoader import JSONLoader
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton
from core.playerClass import PlayerClass


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
        self.getRoot().fadeMenuChange("classConfirmationMenu", "fast")

    def goBack(self):
        self.getRoot().fadeMenuChange("raceSelectionMenu")
