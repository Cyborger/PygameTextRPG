from lib.gui.button import Button


class ImageButton(Button):
    def __init__(self, unhoveredImage, hoveredImage, func, *funcArgs,
                 x=0 , y=0):
        super().__init__(unhoveredImage, func, *funcArgs, x=x, y=y)
        self.unhoveredImage = unhoveredImage
        self.hoveredImage = hoveredImage

    def hover(self):
        self.image = self.hoveredImage

    def unhover(self):
        self.image = self.unhoveredImage
