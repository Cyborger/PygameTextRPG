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
        y = 20
        spacing = 50
        for weapon in weapons:
            self.addButtons(LabelButton(weapon.name, 20, y,
                                        self.weaponSelected, weapon))
            y += spacing
        self.addButtons(LabelButton("Back", 10, y, self.goBack))

    def weaponSelected(self, weapon):
        self.getParent().weaponSelected = weapon
        self.getRoot().fadeMenuChange("attackChoiceMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("battleMenu")
