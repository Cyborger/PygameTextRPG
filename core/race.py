class Race:
    def __init__(self, jsonData):
        self.name = jsonData["Name"]
        self.bonuses = jsonData["StatBonuses"]

    def getBonusesLabel(self):
        string = ""
        for bonus in self.bonuses:
            if self.bonuses[bonus] > 0:
                string += "+" + str(self.bonuses[bonus])
            else:
                string += str(self.bonuses[bonus])
            string += " " + bonus[:3] + "  "
        return string
