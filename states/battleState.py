import pygame
import copy
from menus.battleMenu import BattleMenu
from menus.inventoryMenu import InventoryMenu
from menus.weaponChoiceMenu import WeaponChocieMenu
from menus.attackChoiceMenu import AttackChoiceMenu
from lib.jsonLoader import JSONLoader
from lib.state import State
from lib.gui.label import Label
from lib.gui.surface import Surface
from core.enemy import Enemy


class BattleState(State):
    def __init__(self, game):
        super().__init__("battleState", game)
        self.addMenus(BattleMenu(self), WeaponChocieMenu(self),
                      InventoryMenu(self, "battleMenu"), AttackChoiceMenu(self))
        self.enemies = JSONLoader.loadJSONFile("enemies", Enemy)
        self.currentEnemies = []
        self.selectedWeapon = None

    def newBattle(self, location):
        self.currentEnemies[:] = []
        for enemy in location.enemies:
            for enemyType in self.enemies:
                if enemy == enemyType.name:
                    self.currentEnemies.append(copy.deepcopy(enemyType))
                    self.currentEnemies.append(copy.deepcopy(enemyType))
                    self.currentEnemies.append(copy.deepcopy(enemyType))
        self.getRoot().fadeMenuChange("battleState/battleMenu")

    def getEnemyGUISurfaces(self):
        # Return the images with enemy names and health bars
        surfaces = []
        x = 400
        y = 200
        spacing = 100
        for enemy in self.currentEnemies:
            background = pygame.Surface((400, 75))
            points = [[0, 0], [400, 0], [400, 74], [25, 74]]
            pygame.draw.polygon(background, (255, 255, 255), points, 2)
            nameLabel = Label(enemy.name, 50, 10)
            health = enemy.currentHealth
            maxHealth = enemy.maxHealth
            healthString = str(health) + "/" + str(maxHealth)
            healthLabel  = Label(healthString, 50, 40)
            background.blit(nameLabel.image, nameLabel.rect)
            background.blit(healthLabel.image, healthLabel.rect)
            surfaces.append(Surface(background, x, y))
            y += spacing
        return surfaces
