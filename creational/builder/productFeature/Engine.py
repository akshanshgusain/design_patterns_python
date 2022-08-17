class Engine:

    def __init__(self, volume: float, mileage: float):
        self.volume: float = volume
        self.mileage: float = mileage
        self.started: bool = False

    def on(self):
        self.started: bool = True

    def off(self):
        self.started: bool = False

    def is_started(self) -> bool:
        return self.started

    def get_volume(self) -> float:
        return self.volume

    def get_mileage(self) -> float:
        return self.mileage

    def go(self, mileage: float):
        if self.started:
            self.mileage += mileage
        else:
            print("Cannot go(), you must start engine first!")
