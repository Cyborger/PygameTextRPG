from core.menu import Menu
from core.gui.labelButton import LabelButton

class BattleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("battleMenu", parentState)
        self.addButtons(LabelButton("Attack", 20, 200, self.goToAttackMenu))
        self.addButtons(LabelButton("Inventory", 20, 250, self.goToInventory))
        self.addButtons(LabelButton("Flee", 20, 300, self.attemptToFlee))

    def goToAttackMenu(self):
        print("Attacking")

    def goToInventory(self):
        self.getRoot().fadeMenuChange("inventoryMenu", "fast")

    def attemptToFlee(self):
        print("Attempting to flee")
