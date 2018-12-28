from commands.command_base import CommandBase


class SendEmailCommand(CommandBase):
    def __init__(self, email_service):
        self.email_service = email_service

    def execute(self):
        self.email_service.send()
        return False
