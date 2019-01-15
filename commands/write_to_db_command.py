from sqlalchemy.exc import SQLAlchemyError

from commands.command_base import CommandBase
from infrastructure.exceptions import CommandRuntimeError


class WriteToDbCommand(CommandBase):
    def __init__(self, db_service):
        self.db_service = db_service

    def execute(self):
        try:
            self.db_service.save()
        except SQLAlchemyError:
            raise CommandRuntimeError('SQL Error Save Runtime')
        return True

    def undo(self):
        try:
            self.db_service.delete()
        except SQLAlchemyError:
            raise CommandRuntimeError('SQL Error Delete Runtime')
