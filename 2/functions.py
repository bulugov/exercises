import random


class Rectangle:
    def __init__(self, number, length, width):
        self.length = length
        self.width = width
        self.number = number

    def calculateArea(self):
        """
        Calculates area of the object
        """

        return self.length * self.width


list = [1, 2, 3, 4]


def calculateMinMax():
    """
    Adds several objects of class Rectangle and calculates min/max area
    """
    areas = []

    for i in range(len(list)):
        list[i] = Rectangle(i, random.randint(1, 50), random.randint(1, 50))
    for obj in range(len(list)):
        areas.append(list[obj].calculateArea())

    print(areas)
    max_area = max(areas)
    print("The max area is:", max_area)
    min_area = min(areas)
    print("The min area is:", min_area)


calculateMinMax()
