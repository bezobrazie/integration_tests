import requests
from testData.models.view_models import RegisterVM, LoginVM
from urllib.parse import urljoin


class HttpClientOWF:
    """
    Класс для работы с HTTP запросами
    base_url - базовый урл на который будут поступать запросы
    http://localhost:8000/swagger/index.html
    http://localhost:8000/api-docs/index.html
    """

    REGISTER_ROUTE = "api/auth/register"
    LOGIN_ROUTE = "api/auth/login"

    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, register_vm: RegisterVM) -> requests.Response:
        """
        Метод для регистрации пользователя
        :param register_vm: параметр с моделью данных для регистрации
        :return: объект с информацией об ответе на запрос
        """
        return requests.post(url=urljoin(self.base_url, self.REGISTER_ROUTE), json=register_vm.to_dict())

    def login(self, login_vm: LoginVM) -> requests.Response:
        """
        Метод для авторизации пользователя
        :param login_vm: параметр с моделью данных для авторизации
        :return: объект с информацией об ответе на запрос
        """
        return requests.post(url=urljoin(self.base_url, "api/auth/login"), json=login_vm.to_dict())
