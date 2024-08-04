from behavioral.observer.Display.iDisplayElement import DisplayElement
from behavioral.observer.observer.iObserver import Observer
from behavioral.observer.subject.WeatherData import WeatherData


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        weather_data.register_observer(self)
        self.temperature: float = 0
        self.humidity: float = 0

    #  Callback function
    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity")
