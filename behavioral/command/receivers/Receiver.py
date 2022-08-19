class Receiver:
    def __init__(self):
        self.state: bool = False
        self.label: str = ""

    def on(self):
        self.state = True
        print(f"{self.label} is on")

    def off(self):
        self.state = False
        print(f"{self.label} is off")


class Stereo(Receiver):

    def __init__(self):
        super(Stereo, self).__init__()
        self.label = "Living Room Stereo"


class Light(Receiver):
    def __init__(self, label: str):
        super().__init__()
        self.label = label
