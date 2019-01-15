from infrastructure.exceptions import CommandRuntimeError


class Invoker:
    def __init__(self, commands):
        self.commands = commands
        self.command_history = []

    def execute_commands(self):
        for command in self.commands:
            try:
                self.__execute_command(command)
            except CommandRuntimeError:
                self.__undo_commands()
                return False
        return True

    def __execute_command(self, command):
        if command.execute():
            self.command_history.append(command)

    def __undo_commands(self):
        for i in range(len(self.command_history)):
            command = self.command_history.pop()
            command.undo()
