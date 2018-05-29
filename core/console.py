import pygame
from lib.gui.inputField import InputField


class Console:
    def __init__(self, game):
        self.game = game
        self.currentDisplay = None
        self.textField = InputField(y=600, maxLength=30, fontSize=20)
        self.textField.rect.centerx = 350
        self.textField.showPrompt = True
        self.gettingInput = True

    def loop(self):
        self.currentDisplay = self.game.display.display.copy()
        self.gettingInput = True
        while self.gettingInput:
            self.handleEvents()
            self.render()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gettingInput = False
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.parseCommand()
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_F1:
                    self.gettingInput = False
                elif event.key == pygame.K_BACKSPACE:
                    self.textField.backspace()
                else:
                    self.textField.addInput(event.unicode)

    def render(self):
        self.game.display.clear()
        self.game.display.draw(self.currentDisplay)
        self.game.display.draw(self.textField.image, self.textField.rect)
        pygame.display.flip()

    def parseCommand(self):
        text = self.textField.getContent()
        if len(text) > 0:
            commands = text.split(" ")
            if commands[0] == "changemenu":
                self.game.changeMenu(commands[1])
