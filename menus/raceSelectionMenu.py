from lib.jsonLoader import JSONLoader
from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton
from core.race import Race


class RaceSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceSelectionMenu", parentState)
        self.races = JSONLoader.loadJSONFile("races", Race)
        self.addLabels(Label("Choose a race: ", 10, 20, fontSize=32))
        self.createButtons()

    def createButtons(self):
        x = 40
        y = 70
        ySpacing = 60
        for race in self.races:
            self.addButtons(LabelButton(race.name, x, y, self.chooseRace, race))
            y += ySpacing
        self.addButtons(LabelButton("Back", 20, 650, self.goBack))

    def chooseRace(self, race):
        self.getParent().newPlayer.race = race
        self.getRoot().fadeMenuChange("raceConfirmationMenu", "fast")

    def goBack(self):
        self.getRoot().fadeMenuChange("titleMenuState/titleMenu")
