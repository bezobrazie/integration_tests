from io import BytesIO

import requests
from urllib.parse import urljoin

from testData.models.view_models import RegisterVM, LoginVM, CreateAccountVM, UpdateUserVM
from appDriver.httpDriver.endpoint_variables import EndpointVariables


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

    def create_account(self, token: str, create_account_vm: CreateAccountVM) -> requests.Response:
        """
        Метод для создания нового счета
        :param: :
        """
        return requests.post(url=urljoin(self.base_url, EndpointVariables.CREATE_ACCOUNT_ROUTE),
                             json=create_account_vm.dict(),
                             headers={"Authorization": f"Bearer {token}"})

    def update_user_requisites(self, token: str, update_user_vm: UpdateUserVM) -> requests.Response:
        """
        Метод для создания нового счета
        """
        return requests.post(url=urljoin(self.base_url, EndpointVariables.UPDATE_USER),
                             data=update_user_vm.json(by_alias=True),
                             headers={"Authorization": f"Bearer {token}",
                                      "Content-Type": "application/json"})

    def get_user_requisites(self, token: str) -> requests.Response:
        """
        Метод для получения реквизитов пользователя по токену
        """
        return requests.get(url=urljoin(self.base_url, EndpointVariables.GET_REQUISITES),
                            headers={"Authorization": f"Bearer {token}"})

    def loads_avatar(self, token: str, fp: BytesIO) -> requests.Response:
        return requests.post(url=urljoin(self.base_url, EndpointVariables.AVATAR_ROUTE),
                             headers={"Authorization": f"Bearer {token}"},
                             files={'file': fp})

    def get_avatar(self, token: str) -> requests.Response:
        return requests.get(url=urljoin(self.base_url, EndpointVariables.AVATAR_ROUTE),
                            headers={"Authorization": f"Bearer {token}"})
