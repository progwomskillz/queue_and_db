from requests.exceptions import RequestException

from commands.command_base import CommandBase
from infrastructure.exceptions import CommandRuntimeError


class SendEmailCommand(CommandBase):
    def __init__(self, email_service):
        self.email_service = email_service

    def execute(self):
        try:
            self.email_service.send()
        except RequestException:
            raise CommandRuntimeError('Requests Error')
        return False
