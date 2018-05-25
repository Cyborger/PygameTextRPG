from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton


class PlayerInfoMenu(Menu):
    def __init__(self, parentState):
        super().__init__("playerInfoMenu", parentState)

    def isNowCurrentMenu(self):
        player = self.getRoot().player
        self.labels[:] = []
        self.buttons[:] = []
        self.addLabels(Label("Name: " + player.name),
                       Label("Class: " + player.playerClass.name),
                       Label("Race: " + player.race.name),
                       Label("Health: " + str(player.currentHealth) + " / "
                            + str(player.maxHealth)),
                       Label("Mana: " + str(player.currentMana) + " / "
                            + str(player.maxMana)))
        self.listElements(self.labels, 20, 40)
        self.addButtons(LabelButton("Back", self.goBack, x=10, y=650))

    def goBack(self):
        self.getRoot().fadeMenuChange("mainLocationMenu", "fast")
