class PlayerClass:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.description = jsonData["Description"]

    @classmethod
    def getDefaultPlayerClass(cls):
        return PlayerClass({"Name" : "Default", "Description" : ""})
