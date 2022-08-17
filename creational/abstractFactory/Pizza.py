from abc import ABC, abstractmethod
from typing import List

from creational.abstractFactory.ingredients.iIngredients import *


# Product Class

class Pizza(ABC):
    def __init__(self):
        self.name: str = ''
        self.dough: Dough = Dough()
        self.sauce: Sauce = Sauce()
        self.veggies: List[Veggies] = []
        self.cheese: Cheese = Cheese()
        self.pepperoni: Pepperoni = Pepperoni()
        self.clam: Clams = Clams()

    # We’ve now made the prepare method abstract. This is where we are going to collect the
    # ingredients needed for the pizza, which of course will come from the ingredient factory.
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print(f" Bake for 25 minutes at 360")

    def cut(self):
        print(f"Cutting the pizza into diagonal slices")

    def box(self):
        print(f"Place pizza in official pizza-store box")

    def get_name(self) -> str:
        return self.name
