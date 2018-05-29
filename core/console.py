import pygame
from lib.gui.inputField import InputField
from lib.gui.label import Label


class Console:
    def __init__(self, game):
        self.game = game
        self.currentDisplay = None
        self.textField = InputField(y=600, maxLength=40, fontSize=16)
        self.textField.rect.centerx = 350
        self.textField.showPrompt = True
        self.message = None
        self.gettingInput = True

    def loop(self):
        self.currentDisplay = self.game.display.display.copy()
        self.message = None
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
                elif (event.key == pygame.K_ESCAPE or
                      event.key == pygame.K_BACKQUOTE):
                    self.gettingInput = False
                elif event.key == pygame.K_BACKSPACE:
                    self.textField.backspace()
                else:
                    self.textField.addInput(event.unicode)

    def render(self):
        self.game.display.clear()
        self.game.display.draw(self.currentDisplay)
        self.game.display.draw(self.textField.image, self.textField.rect)
        if self.message is not None:
            self.game.display.draw(self.message.image, self.message.rect)
        pygame.display.flip()

    def parseCommand(self):
        text = self.textField.getContent()
        if len(text) > 0:
            commands = text.split(" ")
            if commands[0] == "changemenu":
                self.changeMenu(commands[1])
            elif commands[0] == "travel":
                self.travel(commands[1])

    def displayMessage(self, text):
        self.message = Label(text, y=575, fontSize=16)
        self.message.rect.centerx = 350

    def changeMenu(self, menuName):
        try:
            self.game.changeMenu(menuName)
            self.gettingInput = False
        except Exception as e:
            self.displayMessage(str(e))

    def travel(self, locationName):
        try:
            location = self.game.locationManager.getLocation(locationName)
            self.game.getState("locationState").currentLocation = location
            self.game.changeMenu("locationState/mainLocationMenu")
            self.gettingInput = False
        except Exception as e:
            self.displayMessage(str(e))
