class Filter():
    def __init__(self, productValue, idealValue = None, temperatures = None):
        self.idealValue = idealValue
        self.productValue = productValue
        if temperatures != None:
            self.temperature_max = temperatures[0]
            self.temperature_min = temperatures[1]

    def filterASC(self):
        if self.productValue > self.idealValue:
            return True
        else:
            return False

    def filterTemperature(self):
        if self.productValue > self.temperature_min and self.productValue < self.temperature_max:
            return True
        else:
            return False
