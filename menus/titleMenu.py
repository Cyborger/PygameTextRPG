from core.menu import Menu
from core.labelButton import LabelButton

class TitleMenu(Menu):
    def __init__(self, game):
        super().__init__("titleMenu", game)
        self.addButton(LabelButton("Continue", 25, 250))
        self.addButton(LabelButton("Begin A New Adventure", 25, 300))
        self.addButton(LabelButton("Exit Game", 25, 350))
