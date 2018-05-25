from lib.menu import Menu
from lib.gui.labelButton import LabelButton


class WeaponChocieMenu(Menu):
    def __init__(self, parentState):
        super().__init__("weaponChoiceMenu", parentState)

    def isNowCurrentMenu(self):
        self.buttons[:] = []
        self.surfaces[:] = []
        self.surfaces.extend(self.getParent().getEnemyGUISurfaces())
        weapons = self.getRoot().player.inventory.getWeapons()
        for weapon in weapons:
            self.addButtons(LabelButton(weapon.name, self.weaponSelected,
                                        weapon))
        self.addButtons(LabelButton("Back", self.goBack))
        self.listElements(self.buttons, 20, 350, align="center")

    def weaponSelected(self, weapon):
        self.getParent().weaponSelected = weapon
        self.getRoot().fadeMenuChange("attackChoiceMenu", "fast")

    def goBack(self):
        self.getRoot().fadeMenuChange("battleMenu", "fast")
