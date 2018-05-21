from core.menu import Menu
from core.gui.multilineLabel import MultilineLabel


class Message(Menu):
    def __init__(self, messages, currentState):
        super().__init__("message", currentState)
        self.stateToReturnTo = currentState.currentMenu
        self.messages = messages
        self.page = 0
        self.generateText()
        self.generateButtons()

    def generateText(self):
        # Generate label from current message
        self.labels[:] = []
        newLabel = MultilineLabel(self.messages[self.page], 0, 200,
                                      600)
        newLabel.rect.centerx = 350
        self.addLabels(newLabel)


    def generateButtons(self):
        # If there are next or previous messages, add arrows to navigate
        self.buttons[:] = []

    def nextMessage(self):
        # if self.page = 0, then size = 1
        self.page += 1
        if self.page > len(self.messages) - 1:
            self.messageEnded()
        else:
            self.generateText()
            self.generateButtons()

    def previousMessage(self):
        self.page = max(self.page - 1, 0)
        self.generateText()
        self.generateButtons()

    def messageEnded(self):
        self.parentState.changeMenu(self.stateToReturnTo)
