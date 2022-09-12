class Counter:
    def __init__(self, name):
        self._name = name
        self._count = 0

    def __str__(self):
        return f"{self._name}: {self._count}"

    def click(self):
        self._count += 1

    def count(self):
        return self._count


clicker = Counter("Clicker")
clicker.click()
clicker.click()
print(clicker.count())
print(clicker)

transistor = Counter("Transistor")
transistor.click()
transistor.click()
transistor.click()
transistor.click()
print(transistor.count())


import math
class Point:
     def __init__(self, x, y):
        self._x = x
        self._y = y