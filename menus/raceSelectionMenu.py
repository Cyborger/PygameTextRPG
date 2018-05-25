from lib.jsonLoader import JSONLoader
from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton
from core.race import Race


class RaceSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceSelectionMenu", parentState)
        self.races = JSONLoader.loadJSONFile("races", Race)
        self.addLabels(Label("Choose a race: ", x=10, y=20, fontSize=32))
        self.createButtons()

    def createButtons(self):
        for race in self.races:
            self.addButtons(LabelButton(race.name, self.chooseRace, race))
        self.listElements(self.buttons, 40, 70, spacing=35)
        self.addButtons(LabelButton("Back", self.goBack, x=20, y=650))

    def chooseRace(self, race):
        self.getParent().newPlayer.race = race
        self.getRoot().fadeMenuChange("raceConfirmationMenu", "fast")

    def goBack(self):
        self.getRoot().fadeMenuChange("titleMenuState/titleMenu")
