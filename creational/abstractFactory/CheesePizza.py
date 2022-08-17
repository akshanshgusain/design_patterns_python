from creational.abstractFactory.Pizza import Pizza
from creational.abstractFactory.iPizzaIngredientFactory import PizzaIngredientFactory


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

