import pickle
import os
import random


class SaveManager:
    def __init__(self):
        self.saves = []
        self.loadSaves()

    def createSave(self, game):
        if self.saveExists(game.currentSaveID):
            self.getSave(game.currentSaveID).update(game)
        else:
            self.createNewSave(game)

    def createNewSave(self, game):
        newID = self.generateRandomID()
        self.saves.append(Save(newID, game))

    def saveExists(self, id_):
        for save in self.saves:
            if save.id_ == id_:
                return True
        return False

    def getSave(self, id_):
        for save in self.saves:
            if save.id_ == id_:
                return save

    def generateRandomID(self):
        id_ = ""
        while True:
            id_ = ""
            for i in range(6):
                id_ += str(random.randint(0, 9))
            if not self.saveExists(id_):
                break
        return id_

    def loadSaves(self):
        self.saves[:] = []
        for file in os.listdir("saves/"):
            if file.endswith(".p"):
                self.saves.append(pickle.load(open("saves/" + file, "rb")))

class Save:
    def __init__(self, id_, game):
        self.id_ = id_
        self.info = {}
        self.update(game)
        self.createFile()

    def update(self, game):
        currentLocation = game.getState("locationState").currentLocation
        self.info = {"player" : game.player, "location" : currentLocation}
        self.createFile()

    def getTitle(self):
        name = self.info["player"].name
        playerClass = self.info["player"].playerClass.name
        return name + " - " + playerClass

    def createFile(self):
        with open("saves/" + self.id_ + ".p", "wb") as f:
            pickle.dump(self, f)

    def load(self, game):
        game.player = self.info["player"]
        game.currentSaveID = self.id_
        game.getState("locationState").currentLocation = self.info["location"]
