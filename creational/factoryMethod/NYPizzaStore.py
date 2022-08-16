from creational.factoryMethod.NYPizza import *
from creational.factoryMethod.PizzaStore import PizzaStore


class NYPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.pizza = None

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            self.pizza = NYStylePizzaCheesePizza()
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
