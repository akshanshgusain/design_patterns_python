import math

from structural.adapter.round.RoundPeg import RoundPeg

# Adapter allows fitting square pegs into round holes.
from structural.adapter.square.SquarePeg import SquarePeg


class SquarePegAdapter(RoundPeg):

    def __init__(self, peg: SquarePeg):
        super().__init__()
        self.peg: SquarePeg = peg

    def get_radius(self) -> float:
        # Calculate a minimum circle radius, which can fit this peg
        return math.sqrt(math.pow(self.peg.get_width() / 2, 2) * 2)
