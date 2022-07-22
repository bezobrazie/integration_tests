import requests


class HttpClientOWF:
    """
    Класс для работы с HTTP запросами
    base_url - базовый урл на который будут поступать запросы
    http://localhost:8000/swagger/index.html
    http://localhost:8000/api-docs/index.html
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, register_data: dict) -> requests.Response:
        """
        Метод для регистрации пользователя
        :param register_data: параметр со словарем в котором передаются данные для регистрации
        """
        return requests.post(self.base_url + "api/auth/register", json=register_data)

    def login(self, login_data: dict) -> requests.Response:
        """
        Метод для авторизации пользователя
        :param login_data: параметр со словарем в котором передаются данные для авторизации
        """
        return requests.post(self.base_url + "api/auth/login", json=login_data)
