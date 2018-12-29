from requests.exceptions import RequestException
from sqlalchemy.exc import SQLAlchemyError

from infrastructure.exceptions import CommandRuntimeError


class Invoker:
    def __init__(self, commands):
        self.commands = commands
        self.command_history = []

    def execute_commands(self):
        for command in self.commands:
            try:
                self.__execute_command(command)
            except RequestException:
                self.__undo_commands()
                message = 'Request error. Check your network connection'
                raise CommandRuntimeError(message)
            except SQLAlchemyError:
                self.__undo_commands()
                message = 'SQL error'
                raise CommandRuntimeError(message)

    def __execute_command(self, command):
        if command.execute():
            self.command_history.append(command)

    def __undo_commands(self):
        for i in range(len(self.command_history)):
            command = self.command_history.pop()
            command.undo()
