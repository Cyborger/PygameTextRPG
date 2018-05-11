from core.menu import Menu
from core.label import Label
from core.labelButton import LabelButton

class PlayerInfoMenu(Menu):
    def __init__(self, parentState):
        super().__init__("playerInfoMenu", parentState)

    def isNowCurrentMenu(self):
        player = self.getParent().player
        self.labels[:] = []
        self.buttons[:] = []
        self.addLabel(Label("Name: " + player.name, 20, 50))
        self.addLabel(Label("Health: " + str(player.currentHealth) + " / "
                            + str(player.maxHealth), 20, 100))
        self.addLabel(Label("Mana: " + str(player.currentMana) + " / "
                            + str(player.maxMana), 20, 150))
        y = 220
        spacing = 60
        statX = 20
        valueX = 350
        for stat in self.getParent().player.stats:
            self.addLabel(Label(stat, statX, y))
            value = player.stats[stat]
            stringValue = str(value)
            if value < 10:
                stringValue = "0" + stringValue
            self.addLabel(Label(stringValue, valueX, y))
            y += spacing
        self.addButton(LabelButton("Back", 10, y, self.goBack))

    def goBack(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                      fadeRate=3)
