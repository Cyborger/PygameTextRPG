from lib.menu import Menu
from lib.gui.label import Label
from lib.gui.labelButton import LabelButton


class LootMenu(Menu):
    def __init__(self, parentState):
        super().__init__("lootMenu", parentState)

    def nowCurrentMenu(self):
        self.labels[:] = []
        self.addLabels(Label("Gold Earned: %s" % self.getParent().goldDrop))
        self.addLabels(Label("Items Dropped: "))
        self.listElements(self.labels, 20, 350, align="center")
        itemListY = self.labels[-1].rect.bottom + 20
        itemLabels = []
        if len(self.getParent().itemDrops) == 0:
            label = Label("None")
            self.addLabels(label)
            itemLabels.append(label)
        else:
            for item in self.getParent().itemDrops:
                label = Label(item.name)
                self.addLabels(label)
                itemLabels.append(label)

        self.listElements(itemLabels, 40, itemListY)

        self.addButtons(LabelButton("Continue", self.nextMenu, x=20, y=600))

    def nextMenu(self):
        self.getRoot().player.inventory.gold += self.getParent().goldDrop
        self.getRoot().player.inventory.addItems(*self.getParent().itemDrops)
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu")
