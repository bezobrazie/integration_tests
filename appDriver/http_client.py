import requests
from urllib.parse import urljoin

from testData.models.view_models import RegisterVM, LoginVM
from appDriver.endpoint_variables import EndpointVariables


class HttpClientOWF:
    """
    Класс для работы с HTTP запросами
    base_url - базовый урл на который будут поступать запросы
    http://localhost:8000/swagger/index.html
    http://localhost:8000/api-docs/index.html
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, register_vm: RegisterVM) -> requests.Response:
        """
        Метод для регистрации пользователя
        :param register_vm: параметр с моделью данных для регистрации
        :return: объект с информацией об ответе на запрос
        """
        return requests.post(url=urljoin(self.base_url, EndpointVariables.REGISTER_ROUTE), json=register_vm.dict())

    def login(self, login_vm: LoginVM) -> requests.Response:
        """
        Метод для авторизации пользователя
        :param login_vm: параметр с моделью данных для авторизации
        :return: объект с информацией об ответе на запрос
        """
        return requests.post(url=urljoin(self.base_url, EndpointVariables.LOGIN_ROUTE), json=login_vm.dict())
