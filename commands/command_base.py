from abc import ABC, abstractmethod

from infrastructure.exceptions import CommandCantBeUndone


class CommandBase(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        raise CommandCantBeUndone('This command cannot be undone')
