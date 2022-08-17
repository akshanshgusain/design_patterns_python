""" Car is a product class. """

from creational.builder.product.CarType import CarType
from creational.builder.productFeature.Engine import Engine
from creational.builder.productFeature.GPSNavigator import GPSNavigator
from creational.builder.productFeature.Transmission import Transmission
from creational.builder.productFeature.TripComputer import TripComputer


class Car:

    def __init__(self, car_type: CarType, seats: int, engine: Engine, transmission: Transmission,
                 trip_computer: TripComputer, gps_navigator: GPSNavigator):
        self.car_type: CarType = car_type
        self.seats: int = seats
        self.engine: Engine = engine
        self.transmission: Transmission = transmission
        self.trip_computer: TripComputer = trip_computer
        self.gps_navigator: GPSNavigator = gps_navigator
        self.fuel: int = 0

    def get_car_type(self) -> CarType:
        return self.car_type

    def get_seats(self) -> int:
        return self.seats

    def set_seats(self, seats: int):
        self.seats = seats

    def set_fuel(self, fuel: int):
        self.fuel = fuel

    def get_fuel(self) -> int:
        return self.fuel

    def get_engine(self) -> Engine:
        return self.engine

    def get_trip_computer(self) -> TripComputer:
        return self.trip_computer

    def get_gps_navigator(self) -> GPSNavigator:
        return self.gps_navigator
