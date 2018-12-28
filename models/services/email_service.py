import requests

from models.environment_settings import EnvironmentSettings


class EmailService:
    def __init__(self, message):
        self.url = EnvironmentSettings.get_var_from_env('EMAIL_URL')
        self.token = EnvironmentSettings.get_var_from_env('EMAIL_TOKEN')
        self.message = message

    def send(self):
        requests.post(self.url, auth=('api', self.token), data=self.message)
