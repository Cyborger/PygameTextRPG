from core.menu import Menu
from core.labelButton import LabelButton


class RaceSelectionMenu(Menu):
    def __init__(self, parentState):
        super().__init__("raceSelectionMenu", parentState)
        self.races = ["Human", "Elf", "Dwarf", "Halfling"]
        self.createButtons()

    def createButtons(self):
        x = 40
        y = 40
        ySpacing = 90
        for race in self.races:
            self.addButton(LabelButton(race, x, y, self.chooseRace, race))
            y += ySpacing
        self.addButton(LabelButton("Back", 20, 650, self.goBack))

    def chooseRace(self, raceName):
        self.getParent().newPlayer.race = raceName
        print("Player race: " + self.getParent().newPlayer.race)

    def goBack(self):
        self.getRoot().fadeMenuChange("characterCreationState/allocateStatsMenu")
