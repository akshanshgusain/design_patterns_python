from abc import ABC

from creational.factoryMethod.Pizza import Pizza


class ChicagoStylePizzaCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")

    def __repr__(self):
        return "NYStyle Cheese Pizza"


class ChicagoStylePizzaPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Sliced seasoned pepperoni")

    def __repr__(self):
        return "NYStyle Pepperoni Pizza"


class ChicagoStylePizzaClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Fresh Water Clams")

    def __repr__(self):
        return "NYStyle Calm Pizza"


class ChicagoStylePizzaVeggiPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Onions")
        self.toppings.append("Broccoli")
        self.toppings.append("Kale")

    def __repr__(self):
        return "NYStyle Veggi Pizza"
