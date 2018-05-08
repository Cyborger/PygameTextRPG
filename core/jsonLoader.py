import json


class JSONLoader:
    def getData(cls, fileName):
        filePath = "json/" + fileName
        with open(fileName) as dataFile:
            return json.load(dataFile)

    def loadJSONFile(cls, fileName):
        objectList = []
        objectData = getData(fileName)
        for obj in objectData:
            objectList.append(objectData[obj])
        return objectList

    def loadRaces(cls):
        for race in loadJSONFile("race"):
