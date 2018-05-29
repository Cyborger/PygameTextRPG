from lib.jsonLoader import JSONLoader
from core.location import Location


class LocationManager:
    def __init__(self):
        self.locations = self.loadLocations()

    def loadLocations(self):
        return JSONLoader.loadJSONFile("locations", Location)

    def getLocation(self, locationName):
        for location in self.locations:
            if location.name.lower() == locationName.lower():
                return location
        raise LocationNotFoundException(locationName.lower())


class LocationNotFoundException(Exception):
    def __init__(self, locationName):
        super().__init__("Unable to find location: " + locationName)
