class Player:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.stats = {"Strength": 10,
                      "Intelligence": 10,
                      "Dexterity": 10,
                      "Charisma": 10,
                      "Luck": 10}

    def printInfo(self):
        print("Name: " + self.name)
        print("Race: " + self.race.name)
        for stat in self.stats:
            print(stat + ": " + str(self.stats[stat]))
