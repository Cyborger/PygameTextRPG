from core.menu import Menu
from core.gui.labelButton import LabelButton
from core.gui.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)
        self.addButtons(LabelButton("Travel", 20, 300, self.goToTravelMenu))
        self.addButtons(LabelButton("Rest", 20, 350, self.rest))
        self.addButtons(LabelButton("Player Stats", 20, 400, self.playerStats))

    def isNowCurrentMenu(self):
        self.surfaces[:] = []
        currentLocationImage = self.getParent().currentLocation.image
        self.addSurfaces(Surface(currentLocationImage, 425, 200))

    def goToTravelMenu(self):
        self.getRoot().fadeMenuChange("travelMenu", "fast")

    def rest(self):
        self.getParent().player.rest()
        self.getRoot().fadeMenuChange("mainLocationMenu", "slow")

    def playerStats(self):
        self.getRoot().fadeMenuChange("playerInfoMenu", "fast")

    def placeholder(self):
        pass
