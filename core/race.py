import pygame


class Race:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.description = jsonData["Description"]

    @classmethod
    def getDefaultRace(cls):
        return Race({"Name" : "Default", "Description" : ""})
