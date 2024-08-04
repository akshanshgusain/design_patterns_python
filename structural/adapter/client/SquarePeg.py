import math


class SquarePeg:
    def __init__(self, width: float):
        self.width = width

    def get_width(self) -> float:
        return self.width

    def get_square(self) -> float:
        return math.pow(self.width, 2)
