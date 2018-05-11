from core.menu import Menu
from core.labelButton import LabelButton


class TravelMenu(Menu):
    def __init__(self, parentState):
        super().__init__("travelMenu", parentState)
        self.updateButtons()

    def updateButtons(self):
        self.buttons[:] = []
        y = 50
        for location in self.getParent().locations:
            if self.getParent().currentLocation is not location:
                self.addButton(LabelButton(location.name, 20, y, self.travel,
                                           location))
                y += 60
        self.addButton(LabelButton("Back", 10, y, self.goBack))

    def travel(self, location):
        self.getParent().currentLocation = location
        self.getRoot().getMenu("locationState/mainLocationMenu").updateSurfaces()
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                      fadeRate=1)
        self.updateButtons()

    def goBack(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu",
                                      fadeRate=4)
