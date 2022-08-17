from creational.abstractFactory.iPizzaIngredientFactory import *
from creational.abstractFactory.ingredients.Ingredients import *


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni()

    def create_clam(self) -> Clams:
        return Clams()