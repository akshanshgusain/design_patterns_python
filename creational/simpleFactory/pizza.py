from abc import ABC


class Pizza(ABC):
    def prepare(self):
        print(f"preparing pizza")

    def bake(self):
        print(f"baking pizza")

    def cut(self):
        print(f"cutting pizza")

    def box(self):
        print(f"boxing pizza")


class CheesePizza(Pizza):
    def __repr__(self):
        return "Cheese Pizza"


class PepperoniPizza(Pizza):
    def __repr__(self):
        return "Pepperoni Pizza"


class ClamPizza(Pizza):
    def __repr__(self):
        return "Calm Pizza"


class VeggiPizza(Pizza):
    def __repr__(self):
        return "Veggi Pizza"
