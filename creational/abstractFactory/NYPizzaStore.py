from creational.abstractFactory.CheesePizza import CheesePizza
from creational.abstractFactory.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from creational.abstractFactory.iPizzaIngredientFactory import PizzaIngredientFactory
from creational.factoryMethod.NYPizza import *
from creational.factoryMethod.PizzaStore import PizzaStore


class NYPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.pizza = None

    # Factory method
    def create_pizza(self, pizza_type: str) -> Pizza:
        # The NY Store is composed with a NY Pizza ingredient factory.
        #  This will be used to produce the ingredients for all NY-Style pizza.
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            self.pizza = CheesePizza(ingredient_factory)
            self.pizza.name = "New York Style Cheese Pizza"
        elif pizza_type == "pepperoni":
            self.pizza = NYStylePizzaPepperoniPizza()
        elif pizza_type == "clam":
            self.pizza = NYStylePizzaClamPizza()
        elif pizza_type == "veggie":
            self.pizza = NYStylePizzaVeggiPizza()
        else:
            self.pizza = NYStylePizzaCheesePizza()

        print(f"created {self.pizza}")
        return self.pizza
