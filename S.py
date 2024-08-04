import math


class Square:
    def __init__(self, lent: int):
        self.length: int = lent


class Circle:
    def __init__(self, rad: int):
        self.radius: int = rad


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes
        self.areas = []

    def sum(self) -> []:
        for shape in self.shapes:
            if shape.__class__.__name__ == "Square":
                self.areas.append(pow(shape.length, 2))
            elif shape.__class__.__name__ == "Circle":
                self.areas.append(math.pi * pow(shape.radius, 2))
        return self.areas

    def output(self):
        areas = self.sum()
        ii = ""
        for area in areas:
            ii += str(area)
            ii += "\n"
        print(ii)


sq = [Square(4), Circle(2)]
area = AreaCalculator(sq)
area.output()
