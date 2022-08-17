""" RoundPegs are compatible with RoundHoles. """


class RoundPeg:
    def __init__(self, radius: float = 0.0):
        self.radius: float = radius

    def get_radius(self) -> float:
        return self.radius
