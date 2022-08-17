from abc import ABC, abstractmethod


# Builder Interface
from creational.builder.product.CarType import CarType
from creational.builder.productFeature.Engine import Engine
from creational.builder.productFeature.GPSNavigator import GPSNavigator
from creational.builder.productFeature.Transmission import Transmission
from creational.builder.productFeature.TripComputer import TripComputer


class Builder(ABC):

    @abstractmethod
    def set_car_type(self, car_type: CarType):
        pass

    @abstractmethod
    def set_seats(self, seats: int):
        pass

    @abstractmethod
    def set_engine(self, engine: Engine):
        pass

    @abstractmethod
    def set_transmission(self, transmission: Transmission):
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer: TripComputer):
        pass

    @abstractmethod
    def set_gps_navigator(self, gps_navigator: GPSNavigator):
        pass
