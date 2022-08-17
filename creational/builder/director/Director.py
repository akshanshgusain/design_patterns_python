"""
 Director defines the order of building steps. It works with a builder object
 through common Builder interface.
 Therefore, it may not know what product is being built.
"""
from creational.builder.iBuilder import Builder
from creational.builder.product.CarType import CarType
from creational.builder.productFeature.Engine import Engine
from creational.builder.productFeature.GPSNavigator import GPSNavigator
from creational.builder.productFeature.Transmission import Transmission
from creational.builder.productFeature.TripComputer import TripComputer


class Director:

    def construct_sports_car(self, builder: Builder):
        builder.set_car_type(CarType.SPORTS_CAR)
        builder.set_seats(2)
        builder.set_engine(Engine(3, 0))
        builder.set_transmission(Transmission.SEMI_AUTOMATIC)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())

    def construct_city_car(self, builder: Builder):
        builder.set_car_type(CarType.CITY_CAR)
        builder.set_seats(5)
        builder.set_engine(Engine(1.2, 0))
        builder.set_transmission(Transmission.AUTOMATIC)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())

    def construct_suv(self, builder: Builder):
        builder.set_car_type(CarType.SUV)
        builder.set_seats(7)
        builder.set_engine(Engine(2.5, 0))
        builder.set_transmission(Transmission.MANUAL)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())
