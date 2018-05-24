from lib.menu import Menu
from lib.gui.button import Button
from lib.gui.labelButton import LabelButton


class AttackChoiceMenu(Menu):
    def __init__(self, parentState):
        super().__init__("attackChoiceMenu", parentState)

    def isNowCurrentMenu(self):
        self.buttons[:] = []
        enemySurfaces = self.getParent().getEnemyGUISurfaces()
        for surface in enemySurfaces:
            index = enemySurfaces.index(surface)
            enemy = self.getParent().currentEnemies[index]
            self.addButtons(EnemyButton(surface, self.enemySelected, enemy))
        self.addButtons(LabelButton("Back", 20, 600, self.goBack))

    def enemySelected(self, enemy):
        damage = self.getParent().weaponSelected.damage
        self.getParent().attackEnemy(enemy, damage)

    def goBack(self):
        self.getRoot().fadeMenuChange("weaponChoiceMenu", "fast")


class EnemyButton(Button):
    def __init__(self, enemyLabel,func, *funcArgs):
        super().__init__(enemyLabel.image, enemyLabel.rect.x, enemyLabel.rect.y,
                         func, *funcArgs)
        self.originalRect = enemyLabel.rect
        self.hoverAmount = 75

    def hover(self):
        self.rect.x = self.originalRect.x - self.hoverAmount

    def unhover(self):
        self.rect.x = self.originalRect.x
