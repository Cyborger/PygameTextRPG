import json
from core.race import Race

class JSONLoader:
    @classmethod
    def getData(cls, fileName):
        filePath = "json/" + fileName + ".json"
        with open(filePath) as dataFile:
            return json.load(dataFile)

    @classmethod
    def loadJSONFile(cls, fileName):
        objectList = []
        objectData = cls.getData(fileName)
        for obj in objectData:
            objectList.append(objectData[obj])
        return objectList

    @classmethod
    def loadRaces(cls):
        raceList = []
        for race in cls.loadJSONFile("races"):
            newRace = Race(race)
            raceList.append(newRace)
        return raceList
