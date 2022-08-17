class TripComputer:
    def __init__(self):
        self.car = None

    def set_car(self, car):
        self.car = car

    def show_fuel_level(self):
        print(f"Fuel level: {self.car.get_fuel()}")

    def show_status(self):
        if self.car.get_engine().is_started():
            print("Car is started")
        else:
            print("Car isn't started")
