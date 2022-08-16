from abc import ABC


# Product Class
class Pizza(ABC):
    def __init__(self):
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing Dough...")
        print(f"Adding Sauce...")
        print(f"Adding Toppings...")
        for topping in self.toppings:
            print(f" {topping}")

    def bake(self):
        print(f" Bake for 25 minutes at 360")

    def cut(self):
        print(f"Cutting the pizza into diagonal slices")

    def box(self):
        print(f"Place pizza in official pizza-store box")

    def get_name(self) -> str:
        return self.name
