import pickle


class SaveManager:
    def __init__(self):
        pass

    def getSaves(self):
        pass

    def loadSave(self, fileName, game):
        saveFile = pickle.load(open(fileName + ".p", "rb"))
        game.player = saveFile["player"]
        game.getState.currentLocation = saveFile["location"]

    def createSave(self, fileName, game):
        saveFile = {"player" : game.player,
                    "location" : game.getState("locationState").currentLocation}
        pickle.dump(open(fileName + ".p", "wb"))
