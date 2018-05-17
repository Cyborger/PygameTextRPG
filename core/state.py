import pygame


class State:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.menus = []
        self.currentMenu = None

    def addMenus(self, *menus):
        for menu in menus:
            self.menus.append(menu)

    def getMenu(self, menuName):
        for menu in self.menus:
            if menu.name == menuName:
                return menu
        raise MenuNotFoundException(menuName)

    def changeMenu(self, menuName):
        self.currentMenu = self.getMenu(menuName)
        self.currentMenu.isNowCurrentMenu()
        self.currentMenu.navigationHandler.buttonSelection = 0
        self.currentMenu.navigationHandler.updateButtons(pygame.mouse.get_pos())
        self.currentMenu.navigationHandler.updateButtonFocus()

    def getRoot(self):
        return self.game

    def resetCurrentMenu(self):
        self.currentMenu.__init__(self)


class MenuNotFoundException(Exception):
    def __init__(self, name):
        super().__init__("Unable to find menu: " + name)
