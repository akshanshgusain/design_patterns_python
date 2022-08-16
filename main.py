from threading import Thread

from creational.singleton.singletone import Singleton
from creational.singleton.singletonThreadSafe import test_singleton
from simpleFactory.pizzaStore import PizzaStore
from simpleFactory.simplePizzaFactory import SimplePizzaFactory

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

if __name__ == "__main__":
    #  Create a factory
    factory: SimplePizzaFactory = SimplePizzaFactory()
    pizzaStore = PizzaStore(factory)
    pizzaStore.order_pizza("clam")
