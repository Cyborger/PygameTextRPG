import json
from core.race import Race

class JSONLoader:
    @classmethod
    def getJSONData(cls, fileName):
        filePath = "json/" + fileName + ".json"
        with open(filePath) as dataFile:
            return json.load(dataFile)

    @classmethod
    def loadJSONFile(cls, fileName, objectClass):
        objectList = []
        data = cls.getJSONData(fileName)
        for obj in data:
            newObj = objectClass(data[obj])
            objectList.append(newObj)
        return objectList
