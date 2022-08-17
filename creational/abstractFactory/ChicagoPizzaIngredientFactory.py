from creational.abstractFactory.iPizzaIngredientFactory import *
from creational.abstractFactory.ingredients.Ingredients import *


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ExtraThickDough()

    def create_sauce(self) -> Sauce:
        return PulmTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni()

    def create_clam(self) -> Clams:
        return Clams()