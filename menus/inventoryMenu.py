from core.menu import Menu
from core.gui.labelButton import LabelButton


class InventoryMenu(Menu):
    def __init__(self, parentState, menuToReturnTo):
        super().__init__("inventoryMenu", parentState)
        self.menuToReturnTo = menuToReturnTo

    def isNowCurrentMenu(self):
        self.buttons[:] = []
        inventory = self.getRoot().player.inventory
        y = 20
        spacing = 50
        for item in inventory.getItems():
            self.addButtons(LabelButton(item.name, 20, y, self.itemSelected,
                                        item))
            y += spacing
        self.addButtons(LabelButton("Back", 20, y, self.goBack))

    def itemSelected(self, item):
        print("Item selected: " + item.name)

    def goBack(self):
        self.getRoot().fadeMenuChange(self.menuToReturnTo, "fast")
