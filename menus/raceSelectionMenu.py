from core.race import Race
from core.jsonLoader import JSONLoader
from core.menu import Menu
from core.label import Label
from core.labelButton import LabelButton


class RaceSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceSelectionMenu", parentState)
        self.races = JSONLoader.loadJSONFile("races", Race)
        self.createLabels()
        self.createButtons()

    def createLabels(self):
        self.addLabel(Label("Choose a race: ", 10, 20, fontSize = 32))

    def createButtons(self):
        x = 40
        y = 70
        ySpacing = 60
        for race in self.races:
            self.addButton(LabelButton(race.name, x, y, self.chooseRace, race))
            y += ySpacing
        self.addButton(LabelButton("Back", 20, 650, self.goBack))

    def chooseRace(self, race):
        self.getParent().newPlayer.race = race
        self.getRoot().fadeMenuChange("characterCreationState/nameChoosingMenu",
                                      fadeRate=3)

    def goBack(self):
        previousMenu = "characterCreationState/allocateStatsMenu"
        self.getRoot().fadeMenuChange(previousMenu, fadeRate=3)
