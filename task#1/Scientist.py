import Worker as worker
from enum import Enum


class Area(Enum):
    Mathematics = 1
    Physics = 2
    Chemistry = 3
    Null = 0


class Type(Enum):
    Theorist = 1
    Experimenter = 2
    Calculator = 3
    Null = 0


class Scientist(worker.Worker):

    def __init__(self):
        super().__init__()
        self.researchArea = Area.Null
        self.papersNumber = 0
        self.type = Type.Null

    def getArea(self):
        return self.researchArea

    def getType(self):
        return self.type

    def getPapersNumber(self):
        return self.papersNumber

    def setArea(self, area):
        self.researchArea = area

    def setType(self, scientist_type):
        self.type = scientist_type

    def setPapersNumber(self, number):
        if number < 0:
            raise ValueError("Can't be negative number")
        self.papersNumber = number

    def printAll(self):
        super().printAll()
        print("\tScientist:")
        print("Research area : ", self.researchArea)
        print("Type : ", self.type)
        print("Number of papers :", self.papersNumber)
