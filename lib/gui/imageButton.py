from lib.gui.button import Button


class ImageButton(Button):
    def __init__(self, image, hoveredImage, func, *funcArgs,
                 x=0 , y=0):
        super().__init__(image, func, *funcArgs, x=x, y=y)
        self.unhoveredImage = unhoveredImage
        self.hoveredImage = hoveredImage

    def hover(self):
        super().hover()
        self.image = self.hoveredImage

    def unhover(self):
        super().unhover()
        self.image = self.unhoveredImage
