from lib.menu import Menu
from lib.gui.labelButton import LabelButton
from lib.gui.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)

    def nowCurrentMenu(self):
        self.surfaces[:] = []
        self.buttons[:] = []
        locationSurface = Surface(self.getParent().currentLocation.image)
        locationSurface.rect.right = 675
        locationSurface.rect.centery = 350
        self.addSurfaces(locationSurface)
        currentLocation = self.getParent().currentLocation

        if currentLocation.hasEnemies():
            func = self.getParent().lookForEnemies
            self.addButtons(LabelButton("Look Around", func))
        if currentLocation.canMine:
            self.addButtons(LabelButton("Mine", self.mine))
        self.addButtons(LabelButton("Travel", self.goToTravelMenu))

        if currentLocation.canRest:
            self.addButtons(LabelButton("Rest", self.rest))
        self.addButtons(LabelButton("Player Stats", self.playerStats),
                        LabelButton("Inventory", self.goToInventory))
        self.listElements(self.buttons, 20, 350, align="center")

    def goToTravelMenu(self):
        self.getRoot().fadeMenuChange("travelMenu", "fast")

    def mine(self):
        ore = self.getRoot().itemManager.getItem("Iron Ore")
        self.getRoot().player.inventory.addItems(ore)
        self.getRoot().fadeMenuChange("mainLocationMenu", "fast")

    def rest(self):
        self.getRoot().player.rest()
        self.getRoot().fadeMenuChange("mainLocationMenu", "slow")

    def playerStats(self):
        self.getRoot().fadeMenuChange("playerInfoMenu", "fast")

    def goToInventory(self):
        self.getRoot().fadeMenuChange("inventoryMenu", "fast")

    def placeholder(self):
        pass
