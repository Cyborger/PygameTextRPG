from core.menu import Menu
from core.labelButton import LabelButton
from core.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)
        self.addButton(LabelButton("Travel", 20, 300, self.goToTravelMenu))
        self.addButton(LabelButton("Rest", 20, 350, self.rest))
        self.addButton(LabelButton("Player Stats", 20, 400, self.playerStats))
        self.updateSurfaces()

    def updateSurfaces(self):
        self.surfaces[:] = []
        self.addSurface(Surface(self.getParent().currentLocation.image, 425, 200))

    def goToTravelMenu(self):
        self.getRoot().changeMenu("locationState/travelMenu")

    def rest(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                      fadeRate = 1)

    def playerStats(self):
        self.getParent().player.printInfo()

    def placeholder(self):
        pass
