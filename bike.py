class Bike():
    def __init__(self):
        self.rider = None
        self.distance = 0

    def start_rental(self, driver):
        if (self.rider == None):
            self.rider = driver
        else:
            raise RuntimeError("There is already a person riding this bike!")

    def bike(self, distance):
        if (self.rider == None):
            raise RuntimeError("There is no rider on this bike!")
        elif (distance < 0):
            raise AttributeError("Distance must be a positive number!")
        else:
            self.distance += distance

    def end_rental(self):
        if (self.rider == None):
            raise RuntimeError("No rental had been started prior!")
        total_distance = self.distance
        self.distance = 0
        self.rider = None
        return total_distance

