from behavioral.command.commands.Commands import Command
from behavioral.command.receivers.Receiver import Light, Stereo


class StereoOffWithCDCommand(Command):

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> bool:
        self.stereo.off()
        return True
