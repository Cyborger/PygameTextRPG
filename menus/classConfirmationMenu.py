from lib.menu import Menu
from lib.gui.multilineLabel import MultilineLabel
from lib.gui.labelButton import LabelButton
from lib.gui.surface import Surface


class ClassConfirmationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("classConfirmationMenu", parentState)
        self.addButtons(LabelButton("Confirm Choice", self.nextMenu),
                        LabelButton("Back", self.goBack))
        self.listElements(self.buttons, 20, 600)

    def nowCurrentMenu(self):
        self.labels[:] = []
        self.surfaces[:] = []
        description = self.getParent().newPlayer.playerClass.description
        descriptionLabel = MultilineLabel(description, x=40, y=40, maxWidth=450)
        self.addLabels(descriptionLabel)
        image = self.getParent().newPlayer.playerClass.getIcon()
        surface = Surface(image, x=450)
        surface.rect.centery = descriptionLabel.rect.centery
        self.addSurfaces(surface)

    def nextMenu(self):
        self.getRoot().fadeMenuChange("nameChoosingMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("classSelectionMenu", "fast")
