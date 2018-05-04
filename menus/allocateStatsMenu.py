from core.menu import Menu
from core.labelButton import LabelButton
from core.imageButton import ImageButton
from core.label import Label

class AllocateStatsMenu(Menu):
    def __init__(self, parentState):
        super().__init__("allocateStatsMenu", parentState)
        self.generateStatLabels()
        self.generateArrows()
        self.addButton(LabelButton("Back", 20, 600, self.goBack))

    def generateStatLabels(self):
        start_y = 38
        xSpacing = 65
        ySpacing = 90
        self.addLabel(Label("Strength      " + str(self.getParent().playerStrength),
                            xSpacing, start_y))
        self.addLabel(Label("Dexterity     " + str(self.getParent().playerDexterity),
                            xSpacing, start_y + ySpacing))
        self.addLabel(Label("Intelligence  " + str(self.getParent().playerIntelligence),
                            xSpacing, start_y + ySpacing * 2))
        self.addLabel(Label("Charisma      " + str(self.getParent().playerCharisma),
                            xSpacing, start_y + ySpacing * 3))
        self.addLabel(Label("Luck          " + str(self.getParent().playerLuck),
                            xSpacing, start_y + ySpacing * 4))

    def generateArrows(self):
        for i in range(5):
            upArrow = ImageButton.fromFilePaths("res/images/upArrowDefault.png",
                                                "res/images/upArrowHovered.png",
                                                20, i * 90 + 20, self.increaseStat)
            downArrow = ImageButton.fromFilePaths("res/images/downArrowDefault.png",
                                                  "res/images/downArrowHovered.png",
                                                  20, i * 90 + 60, self.decreaseStat)
            self.addButton(upArrow)
            self.addButton(downArrow)

    def increaseStat(self):
        print("Increasing stat")

    def decreaseStat(self):
        print("Decreasing stat")

    def goBack(self):
        self.getRoot().fadeMenuChange("titleMenuState/titleMenu", resetMenu=True)
