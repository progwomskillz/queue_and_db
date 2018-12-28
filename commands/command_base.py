from abc import ABC, abstractmethod

from exceptions.commands import CommandCantBeUndone


class CommandBase(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        raise CommandCantBeUndone('This command cannot be undone')
