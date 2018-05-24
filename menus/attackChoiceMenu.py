from lib.menu import Menu
from lib.gui.button import Button


class AttackChoiceMenu(Menu):
    def __init__(self, parentState):
        super().__init__("attackChoiceMenu", parentState)


class EnemyButton(Button):
    def __init__(self):
        pass
