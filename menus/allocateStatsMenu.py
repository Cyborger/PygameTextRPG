import pygame
from core.menu import Menu
from core.labelButton import LabelButton
from core.imageButton import ImageButton
from core.label import Label

#TODO: CLEANUP

class AllocateStatsMenu(Menu):
    def __init__(self, parentState):
        super().__init__("allocateStatsMenu", parentState)
        self.pointsToAllocate = 20
        self.generateLabels()
        self.generateButtons()

    def generateLabels(self):
        statX = 60
        valueX = 450
        y = 70
        spacing = 80
        for stat in self.getParent().newPlayer.stats:
            self.addLabel(Label(stat, statX, y))
            self.addLabel(Label(str(self.getParent().newPlayer.stats[stat]),
                                valueX, y))
            y += spacing
        self.addLabel(Label("Points left: " + str(self.pointsToAllocate),
                            statX, y))

    def generateButtons(self):
        x = 20
        y = 60
        spacing = 50
        arrowSpacing = 30
        upArrow = pygame.image.load("res/images/upArrowDefault.png")
        upArrowHovered = pygame.image.load("res/images/upArrowHovered.png")
        downArrow = pygame.image.load("res/images/downArrowDefault.png")
        downArrowHovered = pygame.image.load("res/images/downArrowHovered.png")
        for stat in self.getParent().newPlayer.stats:
            self.addButton(ImageButton(upArrow, upArrowHovered, x, y,
                                       self.increaseStat, stat))
            y += arrowSpacing
            self.addButton(ImageButton(downArrow, downArrowHovered, x, y,
                                       self.decreaseStat, stat))
            y += spacing
        self.addButton(LabelButton("Continue", x, 600, self.nextMenu))
        self.addButton(LabelButton("Back", x, 650, self.goBack))

    def increaseStat(self, statName):
        if self.pointsToAllocate > 0:
            self.getParent().newPlayer.stats[statName] += 1
            self.pointsToAllocate -= 1
            self.refreshLabels()


    def decreaseStat(self, statName):
        if self.getParent().newPlayer.stats[statName] > 10:
            self.getParent().newPlayer.stats[statName] -= 1
            self.pointsToAllocate += 1
            self.refreshLabels()

    def refreshLabels(self):
        self.labels[:] = []
        self.generateLabels()

    def nextMenu(self):
        self.getRoot().fadeMenuChange("characterCreationState/raceSelectionMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("titleMenuState/titleMenu")
