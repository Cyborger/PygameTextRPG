from lib.menu import Menu
from lib.gui.labelButton import LabelButton

class BattleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("battleMenu", parentState)


    def nowCurrentMenu(self):
        self.surfaces = self.getParent().getEnemyGUISurfaces()
        self.buttons[:] = []
        self.listElements(self.surfaces, 400, 350, align="center")

        if self.getRoot().player.heldWeapon is not None:
            self.addButtons(LabelButton("Attack", self.goToAttackMenu))
        self.addButtons(LabelButton("Inventory", self.goToInventory))
        self.addButtons(LabelButton("Flee", self.attemptToFlee))
        self.listElements(self.buttons, 20, 350, align="center")


    def goToAttackMenu(self):
        self.getRoot().fadeMenuChange("attackChoiceMenu", "fast")

    def goToInventory(self):
        self.getRoot().fadeMenuChange("inventoryMenu", "fast")

    def attemptToFlee(self):
        self.getRoot().fadeMenuChange("locationState/mainLocationMenu", "slow")
