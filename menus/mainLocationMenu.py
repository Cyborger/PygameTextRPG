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

        if self.getParent().currentLocation.hasEnemies():
            func = self.getParent().lookForEnemies
            self.addButtons(LabelButton("Look Around", func))
        self.addButtons(LabelButton("Travel", self.goToTravelMenu))

        if self.getParent().currentLocation.canRest:
            self.addButtons(LabelButton("Rest", self.rest))
        self.addButtons(LabelButton("Player Stats", self.playerStats),
                        LabelButton("Inventory", self.goToInventory))
        self.listElements(self.buttons, 20, 350, align="center")

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
