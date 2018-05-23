from core.menu import Menu
from core.gui.labelButton import LabelButton

class BattleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("battleMenu", parentState)
        self.addButtons(LabelButton("Attack", 20, 300, self.goToAttackMenu))
        self.addButtons(LabelButton("Inventory", 20, 350, self.goToInventory))
        self.addButtons(LabelButton("Flee", 20, 400, self.attemptToFlee))

    def goToAttackMenu(self):
        print("Attacking")

    def goToInventory(self):
        self.getRoot().fadeMenuChange("inventoryMenu", "fast")

    def attemptToFlee(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu", "slow")
