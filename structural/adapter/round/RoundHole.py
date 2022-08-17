# RoundHoles are compatible with RoundPegs
from structural.adapter.round.RoundPeg import RoundPeg


class RoundHole:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        result: bool = self.get_radius() >= peg.get_radius()
        return result
