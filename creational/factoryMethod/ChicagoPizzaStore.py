from creational.factoryMethod.ChicagoPizza import *
from creational.factoryMethod.NYPizza import *
from creational.factoryMethod.PizzaStore import PizzaStore


class ChicagoPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.pizza = None

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            self.pizza = ChicagoStylePizzaCheesePizza()
        elif pizza_type == "pepperoni":
            self.pizza = ChicagoStylePizzaPepperoniPizza()
        elif pizza_type == "clam":
            self.pizza = ChicagoStylePizzaClamPizza()
        elif pizza_type == "veggie":
            self.pizza = ChicagoStylePizzaVeggiPizza()
        else:
            self.pizza = ChicagoStylePizzaCheesePizza()

        print(f"created {self.pizza}")
        return self.pizza
