from behavioral.observer.observer.iObserver import Observer
from behavioral.observer.subject.iSubject import Subject


class WeatherData(Subject):

    def __init__(self):
        self.observers: list[Observer] = []
        self.temperature: float = 0
        self.humidity: float = 0
        self.pressure: float = 0

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
