from creational.abstractFactory.CheesePizza import CheesePizza
from creational.abstractFactory.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory
from creational.abstractFactory.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from creational.abstractFactory.Pizza import Pizza
from creational.factoryMethod.NYPizzaStore import NYPizzaStore
from creational.factoryMethod.PizzaStore import PizzaStore

''' Singleton test code'''

# if __name__ == "__main__":
#     oS1 = Singleton()
#     oS2 = Singleton()
#
#     if id(oS1) == id(oS2):
#         print("Singleton works, both variables contain the same instance.")
#     else:
#         print("Singleton failed, variables contain different instances.")

''' Singleton-ThreadSafe test code'''

# if __name__ == "__main__":
#     print("If you see the same value, then singleton was reused (yay!)\n"
#           "If you see different values, "
#           "then 2 singletons were created (booo!!)\n\n"
#           "RESULT:\n")
#
#     process1 = Thread(target=test_singleton, args=("John",))
#     process2 = Thread(target=test_singleton, args=("Doe",))
#     process1.start()
#     process2.start()

""" Simple Factory test code"""

# if __name__ == "__main__":
#     #  Create a factory
#     factory: SimplePizzaFactory = SimplePizzaFactory()
#     # Create the pizza store and  pass the factory to the pizza store
#     pizzaStore = PizzaStore(factory)
#     pizzaStore.order_pizza("clam")

""" Factory Method test code """

# if __name__ == "__main__":
#     ny_pizza_store: PizzaStore = NYPizzaStore()
#     ny_pizza_store.order_pizza('pepperoni')
#     ny_pizza_store.order_pizza('cheese')
#
#     chicago_pizza_store: PizzaStore = ChicagoPizzaStore()
#     chicago_pizza_store.order_pizza('cheese')

""" Abstract Factory test code"""

if __name__ == "__main__":
    pizza_store: PizzaStore = NYPizzaStore()
    # pizza = pizza_store.create_pizza("pepperoni")
    pizza = pizza_store.order_pizza("pepperoni")

    # or Abstract Factory - Ingredient factory
    # create ingredient factories
    ny_ingredient_factory: NYPizzaIngredientFactory = NYPizzaIngredientFactory()
    chicago_ingredient_factory: ChicagoPizzaIngredientFactory = ChicagoPizzaIngredientFactory()

    ny_cheese_pizza: Pizza = CheesePizza(ny_ingredient_factory)
    ny_cheese_pizza.prepare()
    ny_cheese_pizza.bake()
    ny_cheese_pizza.cut()
    ny_cheese_pizza.box()
