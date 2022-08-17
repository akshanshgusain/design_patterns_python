from structural.decorator.decorators.iCondimentDecorator import CondimentDecorator
from structural.decorator.iBeverage import Beverage


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20
