from abc import ABC, abstractmethod

from exceptions.commands.command_cant_be_undone import CommandCantBeUndone


class CommandBase(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        raise CommandCantBeUndone('This command cannot be undone')
