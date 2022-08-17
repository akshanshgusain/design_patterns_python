from creational.simpleFactory.pizza import Pizza
from creational.simpleFactory.simplePizzaFactory import SimplePizzaFactory


class PizzaStore:

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza = self.factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
