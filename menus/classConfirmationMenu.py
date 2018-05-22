from core.menu import Menu
from core.gui.multilineLabel import MultilineLabel
from core.gui.labelButton import LabelButton
from core.gui.surface import Surface


class ClassConfirmationMenu(Menu):
    def __init__(self, parentState):
        super().__init__("classConfirmationMenu", parentState)
        self.addButtons(LabelButton("Confirm Choice", 20, 600, self.nextMenu),
                        LabelButton("Back", 20, 650, self.goBack))

    def isNowCurrentMenu(self):
        self.labels[:] = []
        self.surfaces[:] = []
        description = self.getParent().newPlayer.playerClass.description
        descriptionLabel = MultilineLabel(description, 40, 40, maxWidth=450)
        self.addLabels(descriptionLabel)
        image = self.getParent().newPlayer.playerClass.getIcon()
        surface = Surface(image, 475, 0)
        surface.rect.centery = descriptionLabel.rect.centery
        self.addSurfaces(surface)

    def nextMenu(self):
        self.getRoot().fadeMenuChange("nameChoosingMenu")

    def goBack(self):
        self.getRoot().fadeMenuChange("classSelectionMenu", "fast")
