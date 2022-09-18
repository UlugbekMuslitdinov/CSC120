class Temp:

    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit

    def __str__(self):
        return str(self._temp) + str(self._unit)

    def to_Celcius(self):
        if self._unit == 'C':
            return self._temp
        elif self._unit == 'F':
            return (self._temp - 32) * 5 / 9
        else:
            return self._temp

    def __eq__(self, other):
        return self.to_Celcius() == other.to_Celcius()

    def __lt__(self, other):
        return self.to_Celcius() < other.to_Celcius()

    def __gt__(self, other):
        return self.to_Celcius() > other.to_Celcius()

    def __ne__(self, other):
        return self.to_Celcius() != other.to_Celcius()


