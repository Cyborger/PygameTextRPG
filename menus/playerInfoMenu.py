from core.menu import Menu
from core.gui.label import Label
from core.gui.labelButton import LabelButton


class PlayerInfoMenu(Menu):
    def __init__(self, parentState):
        super().__init__("playerInfoMenu", parentState)

    def isNowCurrentMenu(self):
        player = self.getParent().player
        self.labels[:] = []
        self.buttons[:] = []
        self.addLabels(Label("Name: " + player.name, 20, 50),
                       Label("Class: " + player.playerClass.name, 20, 100),
                       Label("Race: " + player.race.name, 20, 150),
                       Label("Health: " + str(player.currentHealth) + " / "
                            + str(player.maxHealth), 20, 200),
                       Label("Mana: " + str(player.currentMana) + " / "
                            + str(player.maxMana), 20, 250))
        self.addButtons(LabelButton("Back", 10, 650, self.goBack))

    def goBack(self):
        self.getRoot().fadeMenuChange("mainLocationMenu", "fast")
