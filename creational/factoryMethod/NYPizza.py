from abc import ABC

from creational.factoryMethod.Pizza import Pizza


class NYStylePizzaCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")

    def __repr__(self):
        return "NYStyle Cheese Pizza"


class NYStylePizzaPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Sliced seasoned pepperoni")

    def __repr__(self):
        return "NYStyle Pepperoni Pizza"


class NYStylePizzaClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Fresh Water Clams")

    def __repr__(self):
        return "NYStyle Calm Pizza"


class NYStylePizzaVeggiPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Onions")
        self.toppings.append("Broccoli")
        self.toppings.append("Kale")

    def __repr__(self):
        return "NYStyle Veggi Pizza"
