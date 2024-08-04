import math
from structural.adapter.round.RoundPeg import RoundPeg
from structural.adapter.client.SquarePeg import SquarePeg

# Adapter allows fitting client pegs into round holes.
"""
Adapter is a structural design pattern, which allows incompatible objects to collaborate.
The Adapter acts as a wrapper between two objects. It catches calls for one object and transforms them to format and interface recognizable by the second object.
"""


class SquarePegAdapter(RoundPeg):

    def __init__(self, peg: SquarePeg):
        super().__init__()
        self.peg: SquarePeg = peg

    def get_radius(self) -> float:
        # Calculate a minimum circle radius, which can fit this peg
        return math.sqrt(math.pow(self.peg.get_width() / 2, 2) * 2)
