import requests


class HttpClientOWF:

    """ Клиент для осуществления HTTP запросов на OWF """

    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, register_data: dict) -> requests.Response:
        return requests.post(self.base_url + "api/auth/register", json=register_data)

    def login(self, login_data) -> requests.Response:
        return requests.post(self.base_url + "api/auth/login", json=login_data)
