from core.inventory import Inventory
from core.race import Race
from core.playerClass import PlayerClass


class Player:
    def __init__(self):
        self.name = "Default"
        self.playerClass = PlayerClass.getDefaultPlayerClass()
        self.race = Race.getDefaultRace()
        self.currentHealth = 10
        self.maxHealth = 20
        self.currentMana = 10
        self.maxMana = 20
        self.inventory = Inventory()
        self.heldWeapon = None

    def rest(self):
        self.currentHealth = self.maxHealth
        self.currentMana = self.maxMana
