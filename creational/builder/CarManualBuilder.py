from creational.builder.iBuilder import Builder
from creational.builder.product.CarType import CarType
from creational.builder.product.Manual import Manual
from creational.builder.productFeature.Engine import Engine
from creational.builder.productFeature.GPSNavigator import GPSNavigator
from creational.builder.productFeature.Transmission import Transmission
from creational.builder.productFeature.TripComputer import TripComputer

"""
Unlike other creational patterns, Builder can construct unrelated products,
which don't have the common interface.

In this case we build a user manual for a car, using the same steps as we
built a car. This allows to produce manuals for specific car models,
configured with different features.

"""


class CarManualBuilder(Builder):
    def __init__(self):
        self.car_type: CarType = None
        self.seats: int = 0
        self.engine: Engine = None
        self.transmission: Transmission = None
        self.trip_computer: TripComputer = None
        self.gps_navigator: GPSNavigator = None

    def set_car_type(self, car_type: CarType):
        self.car_type = car_type

    def set_seats(self, seats: int):
        self.seats = seats

    def set_engine(self, engine: Engine):
        self.engine = engine

    def set_transmission(self, transmission: Transmission):
        self.transmission = transmission

    def set_trip_computer(self, trip_computer: TripComputer):
        self.trip_computer = trip_computer

    def set_gps_navigator(self, gps_navigator: GPSNavigator):
        self.gps_navigator = gps_navigator

    def get_result(self) -> Manual:
        return Manual(self.car_type, self.seats, self.engine, self.transmission, self.trip_computer, self.gps_navigator)
