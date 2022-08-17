from abc import ABC, abstractmethod

from creational.simpleFactory.pizza import Pizza

"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.
"""

"""
The Factory Method pattern suggests that you replace direct object construction calls (using the new operator) with 
calls to a special factory method. Don’t worry: the objects are still created via the new operator, but it’s being
called from within the factory method. Objects returned by a factory method are often referred to as products.
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
