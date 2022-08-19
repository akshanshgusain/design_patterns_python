
from behavioral.command.commands.Commands import Command
from behavioral.command.receivers.Receiver import Light


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self) -> bool:
        self.light.on()
        return True
