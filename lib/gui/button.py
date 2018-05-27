from lib.gui.surface import Surface


class Button(Surface):
    def __init__(self, image, func, *funcArgs, x=0, y=0):
        super().__init__(image, x=x, y=y)
        self.hovered = False
        self.click = func
        self.funcArgs = funcArgs

    def update(self, mousePosition):
        if self.isHovering(mousePosition) and not self.hovered:
            self.hover()
            self.hovered = True
        elif not self.isHovering(mousePosition) and self.hovered:
            self.unhover()
            self.hovered = False

    def isHovering(self, mousePosition):
        if self.rect.collidepoint(mousePosition):
            return True
        return False

    def checkForClick(self):
        if self.hovered:
            self.click(*self.funcArgs)

    def hover(self):
        self.hovered = True

    def unhover(self):
        self.hovered = False


    def click(self):
        pass
