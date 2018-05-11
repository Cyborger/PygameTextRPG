from core.menu import Menu
from core.labelButton import LabelButton
from core.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)
        self.addButton(LabelButton("Travel", 20, 300, self.goToTravelMenu))
        self.addButton(LabelButton("Rest", 20, 350, self.rest))
        self.addButton(LabelButton("Player Stats", 20, 400, self.playerStats))

    def isNowCurrentMenu(self):
        self.surfaces[:] = []
        currentLocationImage = self.getParent().currentLocation.image
        self.addSurface(Surface(currentLocationImage, 425, 200))

    def goToTravelMenu(self):
        self.getRoot().fadeMenuChange("locationState/travelMenu", fadeRate=4)

    def rest(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                      fadeRate = 1)

    def playerStats(self):
        self.getRoot().fadeMenuChange("locationState/playerInfoMenu",
                                      fadeRate=3)

    def placeholder(self):
        pass
