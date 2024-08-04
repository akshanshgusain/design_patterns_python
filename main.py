from structural.decorator.DarkRoast import DarkRoast
from structural.decorator.Espresso import Espresso
from structural.decorator.decorators.Mocha import Mocha
from structural.decorator.decorators.Soy import Soy
from structural.decorator.decorators.Whip import Whip
from structural.decorator.iBeverage import Beverage

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

# if __name__ == "__main__":

#
#     # or Abstract Factory - Ingredient factory
#     # create ingredient factories
#     ny_ingredient_factory: NYPizzaIngredientFactory = NYPizzaIngredientFactory()
#     chicago_ingredient_factory: ChicagoPizzaIngredientFactory = ChicagoPizzaIngredientFactory()
#
#     ny_cheese_pizza: Pizza = CheesePizza(ny_ingredient_factory)
#     ny_cheese_pizza.prepare()
#     ny_cheese_pizza.bake()
#     ny_cheese_pizza.cut()
#     ny_cheese_pizza.box()

""" Builder test code"""

# if __name__ == "__main__":
#     director: Director = Director()
#
#     # Director gets the concrete builder object from the client
#     # (application code). That's because application knows better which
#     # builder to use to get a specific product.
#     car_builder: CarBuilder = CarBuilder()
#     director.construct_sports_car(car_builder)
#
#     # The final product is often retrieved from a builder object, since
#     # Director is not aware and not dependent on concrete builders and products.
#     car: Car = car_builder.get_result()
#     print(f"Car built: \n {car.get_car_type()}")
#
#     manual_builder: CarManualBuilder = CarManualBuilder()
# #     Director may know several building recipes'
#     director.construct_sports_car(manual_builder)
#     manual_car: Manual = manual_builder.get_result()
#     print(f"Manual Car built: \n {manual_car}")

""" Adapter test code """

# if __name__ == "__main__":
#     # Round fits round, no surprise.
#     round_hole: RoundHole = RoundHole(9)
#     round_peg: RoundPeg = RoundPeg(9)
#     if round_hole.fits(round_peg):
#         print(f"Round peg r9 fits round hole r9")
#
#     small_square_peg: SquarePeg = SquarePeg(2)
#     large_square_peg: SquarePeg = SquarePeg(12)
#
#     # round_hole.fits(small_square_peg)
#     # Expected type 'RoundPeg', got 'SquarePeg' instead
#     # Adapter Solves this problem =>
#     small_square_peg_adapter: SquarePegAdapter = SquarePegAdapter(small_square_peg)
#     large_square_peg_adapter: SquarePegAdapter = SquarePegAdapter(small_square_peg)
#
#     if round_hole.fits(small_square_peg_adapter):
#         print("Square peg w2 fits round hole r5")
#     if not round_hole.fits(large_square_peg_adapter):
#         print("Square peg w20 does not fit into round hole r5.")


""" Decorator test code"""

if __name__ == "__main__":
    beverage: Beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    beverage_2: Beverage = DarkRoast()
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    beverage_2 = Soy(beverage_2)
    print(f"{beverage_2.get_description()} ${beverage_2.cost()}")

""" Facade test code"""

# if __name__ == "__main__":
#     converter: VideoConversionFacade = VideoConversionFacade()
#     mp4_file: str = converter.convert_video("ducktyping.ogg", "mp4")
#     print(mp4_file)


""" Proxy test code """
# if __name__ == "__main__":
#     application: Application = Application()
#     supported_methods: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
#     nginx: Nginx = Nginx(application, 5, supported_methods)
#
#     # Making requests
#     print(nginx.handle_request("/some/wrong/url", "GET"))
#     print(nginx.handle_request("/app/status", "FOO"))
#     print(nginx.handle_request("/app/status", "POST"))
#     print(nginx.handle_request("/app/status", "GET"))
#     print(nginx.handle_request("/app/status", "GET"))
#     print(nginx.handle_request("/app/status", "GET"))
#     print(nginx.handle_request("/app/status", "GET"))
#     print(nginx.handle_request("/app/status", "GET"))
#
#     print(nginx.handle_request("/create/user", "POST"))
#     print(nginx.handle_request("/create/user", "GET"))
#     print(nginx.handle_request("/create/user", "BAR"))


""" Observer test code """

# if __name__ == "__main__":
#     # Subject :
#     weather_data: WeatherData = WeatherData()
#
#     # Observer and Display :
#     current_display: CurrentConditionDisplay = CurrentConditionDisplay(weather_data)
#
#     weather_data.set_measurements(80, 65, 30.4)
#     weather_data.set_measurements(82, 70, 34.2)
#     weather_data.set_measurements(78, 90, 27.7)

""" Strategy test code """

# if __name__ == "__main__":
#     PRICE_ON_PRODUCTS: dict[int, float] = {1: 2200, 2: 1850, 3: 1100, 4: 890}
#     ORDER: Order = Order()
#     STRATEGY = None
#
#     while not ORDER.is_closed():
#         cost: float
#         continue_choice: str
#
#         while True:
#             choice = input("Please, select a product:" + "\n" +
#                            "1 - Mother board" + "\n" +
#                            "2 - CPU" + "\n" +
#                            "3 - HDD" + "\n" +
#                            "4 - Memory" + "\n")
#             cost = PRICE_ON_PRODUCTS.get(int(choice), 1)
#             count = int(input("Count: "))
#             ORDER.set_total_cost(cost * count)
#             continue_choice = input("Do you wish to continue selecting products? Y/N: ")
#             if continue_choice == "n" or continue_choice == "N":
#                 break
#             else:
#                 continue
#
#         payment_method: str = input("Please, select a payment method:" + "\n" +
#                                     "1 - PalPay" + "\n" +
#                                     "2 - Credit Card")
#         # Client creates different strategies based on input from user,
#         # application configuration, etc
#
#         #  Improvement = factory method
#         if payment_method == "1":
#             strategy = PayByPayPal()
#         else:
#             strategy = PayByCreditCard()
#
#         # Order object delegates gathering payment data to strategy object,
#         # since only strategies know what data they need to process a payment.
#         ORDER.process_order(strategy)
#         proceed = input(f"Pay {ORDER.get_total_cost()} units or continue shopping? P/C: ")
#
#         if proceed == "P" or proceed == "p":
#             # finally, strategy handles the payment.
#             if strategy.pay(ORDER.get_total_cost()):
#                 print("Payment has been successful.")
#             else:
#                 print("Payment has failed.")
#         ORDER.set_close()

"""Command test code"""

# if __name__ == "__main__":
#     remote: RemoteControl = RemoteControl(4)
#
#     # Command receivers
#     living_room_light: Light = Light("Living Room Light")
#     bed_room_light: Light = Light("Bed Room Light")
#     kitchen_room_light: Light = Light("Kitchen Room Light")
#     stereo: Stereo = Stereo()
#
#     # Commands
#     living_room_light_on_command: Command = LightOnCommand(living_room_light)
#     living_room_light_off_command: Command = LightOffCommand(living_room_light)
#
#     bed_room_light_on_command: Command = LightOnCommand(bed_room_light)
#     bed_room_light_off_command: Command = LightOffCommand(bed_room_light)
#
#     kitchen_room_light_on_command: Command = LightOnCommand(kitchen_room_light)
#     kitchen_room_light_off_command: Command = LightOffCommand(kitchen_room_light)
#
#     stereo_on_command: Command = StereoOnWithCDCommand(stereo)
#     stereo_off_command: Command = StereoOffWithCDCommand(stereo)
#
#     # Set commands to remote control
#
#     remote.set_command(0, living_room_light_on_command, living_room_light_off_command)
#     remote.set_command(1, bed_room_light_on_command, bed_room_light_off_command)
#     remote.set_command(2, kitchen_room_light_on_command, kitchen_room_light_off_command)
#     remote.set_command(3, stereo_on_command, stereo_off_command)
#
#     print(remote)
#
#     remote.on_button_pushed(3)
#     remote.on_button_pushed(2)
#     remote.off_button_pushed(2)
