from creational.simpleFactory.pizza import *


class SimplePizzaFactory:
    def __init__(self):
        self.pizza = None

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            self.pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            self.pizza = PepperoniPizza()
        elif pizza_type == "clam":
            self.pizza = ClamPizza()
        elif pizza_type == "veggie":
            self.pizza = VeggiPizza()
        else:
            self.pizza = CheesePizza()

        print(f"created {self.pizza}")
        return self.pizza
