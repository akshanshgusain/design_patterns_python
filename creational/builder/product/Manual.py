from creational.builder.product.CarType import CarType
from creational.builder.productFeature.Engine import Engine
from creational.builder.productFeature.GPSNavigator import GPSNavigator
from creational.builder.productFeature.Transmission import Transmission
from creational.builder.productFeature.TripComputer import TripComputer


class Manual:
    def __init__(self, car_type: CarType, seats: int, engine: Engine, transmission: Transmission,
                 trip_computer: TripComputer, gps_navigator: GPSNavigator):
        self.car_type: CarType = car_type
        self.seats: int = seats
        self.engine: Engine = engine
        self.transmission: Transmission = transmission
        self.trip_computer: TripComputer = trip_computer
        self.gps_navigator: GPSNavigator = gps_navigator
        self.fuel: int = 0

    def __repr__(self):
        info: str = f"Type of car: {self.car_type}\n " \
                    f"Count of seats: {self.seats}\n" \
                    f"Engine: Volume: {self.engine.get_volume()}; mileage: {self.engine.get_mileage()}\n" \
                    f"Transmission: {self.transmission}\n"
        if self.trip_computer is not None:
            info += f"Trip Computer: Functional \n"
        else:
            info += f"GPS Navigation: Functional\n"
        if self.gps_navigator is not None:
            info += f"GPS Navigator: Functional\n"
        else:
            info += f"GPS Navigator: N/A\n"
        return info
