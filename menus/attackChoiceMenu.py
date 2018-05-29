from lib.menu import Menu
from lib.gui.button import Button
from lib.gui.labelButton import LabelButton


class AttackChoiceMenu(Menu):
    def __init__(self, parentState):
        super().__init__("attackChoiceMenu", parentState)

    def nowCurrentMenu(self):
        self.buttons[:] = []
        enemySurfaces = self.getParent().getEnemyGUISurfaces()
        self.listElements(enemySurfaces, 400, 350, align="center")
        for surface in enemySurfaces:
            index = enemySurfaces.index(surface)
            enemy = self.getParent().currentEnemies[index]
            self.addButtons(EnemyButton(surface, self.enemySelected, enemy))
        self.addButtons(LabelButton("Back", self.goBack, x=20, y=600))

    def enemySelected(self, enemy):
        enemy.takeDamage(self.getRoot().player.heldWeapon.damage)
        if enemy.isDead():
            self.getParent().calculateEnemyDrops(enemy)
            self.getParent().currentEnemies.remove(enemy)
        if len(self.getParent().currentEnemies) == 0:
            self.getRoot().fadeMenuChange("lootMenu")
        else:
            self.getRoot().fadeMenuChange("battleMenu", "fast")

    def goBack(self):
        self.getRoot().fadeMenuChange("battleMenu", "fast")


class EnemyButton(Button):
    def __init__(self, enemyLabel,func, *funcArgs):
        super().__init__(enemyLabel.image, func, *funcArgs, x=enemyLabel.rect.x,
                         y=enemyLabel.rect.y)
        self.originalRect = enemyLabel.rect
        self.hoverAmount = 75

    def hover(self):
        super().hover()
        self.rect.x = self.originalRect.x - self.hoverAmount

    def unhover(self):
        super().unhover()
        self.rect.x = self.originalRect.x
