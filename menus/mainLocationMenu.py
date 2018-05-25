from lib.menu import Menu
from lib.gui.labelButton import LabelButton
from lib.gui.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)

    def isNowCurrentMenu(self):
        self.surfaces[:] = []
        self.buttons[:] = []
        currentLocationImage = self.getParent().currentLocation.image
        self.addSurfaces(Surface(currentLocationImage, 425, 200))

        buttons = []
        if self.getParent().currentLocation.hasEnemies():
            func = self.getParent().lookForEnemies
            buttons.append(LabelButton("Look Around", 0, 0, func))
        buttons.append(LabelButton("Travel", 0, 0, self.goToTravelMenu))
        if self.getParent().currentLocation.canRest:
            buttons.append(LabelButton("Rest", 0, 0, self.rest))
        buttons.append(LabelButton("Player Stats", 0, 0, self.playerStats))
        buttons.append(LabelButton("Inventory", 0, 0, self.goToInventory))
        self.createButtonList(buttons, 20, 300, 50)

    def goToTravelMenu(self):
        self.getRoot().fadeMenuChange("travelMenu", "fast")

    def rest(self):
        self.getRoot().player.rest()
        self.getRoot().fadeMenuChange("mainLocationMenu", "slow")

    def playerStats(self):
        self.getRoot().fadeMenuChange("playerInfoMenu", "fast")

    def goToInventory(self):
        self.getRoot().fadeMenuChange("inventoryMenu", "fast")

    def placeholder(self):
        pass
