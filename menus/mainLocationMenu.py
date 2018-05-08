from core.menu import Menu
from core.labelButton import LabelButton
from core.surface import Surface


class MainLocationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("mainLocationMenu", parentState)
        self.addButton(LabelButton("Travel", 20, 300, self.placeholder))
        self.addButton(LabelButton("Rest", 20, 350, self.placeholder))
        self.addButton(LabelButton("Check Inventory", 20, 400, self.placeholder))
        self.addLabel(Surface("res/images/campfire.png", 425, 200))

    def placeholder(self):
        print("Currently a placeholder")
