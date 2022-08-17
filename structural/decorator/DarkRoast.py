from structural.decorator.iBeverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast"

    def cost(self) -> float:
        return 0.99
