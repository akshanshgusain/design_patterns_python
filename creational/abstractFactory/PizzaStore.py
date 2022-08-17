from abc import ABC, abstractmethod

from simpleFactory.pizza import Pizza

"""
Abstract Factory defines an interface for creating all distinct products but leaves the actual product creation to
concrete factory classes. Each factory type corresponds to a certain product variety.
"""


#  Creator Class
class PizzaStore(ABC):

    def __init__(self):
        pass

    # Factory Method
    # Our Factory Method is now abstract
    @abstractmethod
    def create_pizza(self, pizza_type: str):
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza = self.create_pizza(pizza_type)  # previously call to the simple-factory

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


"""
Now we’ve got a store waiting for subclasses; we’re going to have a subclass for each regional type 
(NYPizzaStore, ChicagoPizzaStore, CaliforniaPizzaStore) and each subclass is going to make the decision about what
 makes up a pizza. Let’s take a look at how this is going to work.
"""
