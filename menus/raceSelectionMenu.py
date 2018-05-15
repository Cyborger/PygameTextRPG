from core.race import Race
from core.jsonLoader import JSONLoader
from core.menu import Menu
from core.gui.label import Label
from core.gui.labelButton import LabelButton


class RaceSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceSelectionMenu", parentState)
        self.races = JSONLoader.loadJSONFile("races", Race)
        self.addLabels(Label("Choose a race: ", 10, 20, fontSize = 32))
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
        nextMenu = "characterCreationState/raceConfirmationMenu"
        self.getRoot().fadeMenuChange(nextMenu, fadeRate=3)

    def goBack(self):
        previousMenu = "titleMenuState/titleMenu"
        self.getRoot().fadeMenuChange(previousMenu, fadeRate=3)
