import requests


class EmailService:
    def __init__(self, environment_manager, message):
        self.url = environment_manager.get_var_from_env('EMAIL_URL')
        self.token = environment_manager.get_var_from_env('EMAIL_TOKEN')

        self.message = message

    def send(self):
        requests.post(self.url, auth=('api', self.token), data=self.message)
