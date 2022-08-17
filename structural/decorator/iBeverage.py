from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.description: str = "unknown beverage"

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass
