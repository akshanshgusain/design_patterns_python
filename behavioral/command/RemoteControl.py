from behavioral.command.commands.Commands import Command, NoCommand


class RemoteControl:

    def __init__(self, number_of_commands: int):
        self.on_commands: list[Command] = []
        self.off_commands: list[Command] = []
        no_command: Command = NoCommand()
        for i in range(number_of_commands):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> bool:
        return self.on_commands[slot].execute()

    def off_button_pushed(self, slot: int) -> bool:
        return self.off_commands[slot].execute()

    def __repr__(self) -> str:
        rep: str = f"\n------------- Remote Control ---------------- \n"
        for i in range(len(self.on_commands)):
            rep += f"[slot: {i}] {self.on_commands[i].__class__.__name__} \t {self.off_commands[i].__class__.__name__} \n"
        return rep
