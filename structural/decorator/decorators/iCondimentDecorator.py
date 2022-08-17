from abc import abstractmethod
from structural.decorator.iBeverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self):
        super().__init__()
        self.beverage = None

    @abstractmethod
    def get_description(self) -> str:
        pass
