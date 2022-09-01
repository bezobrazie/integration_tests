import pytest
import requests
from syrupy.filters import paths

from testData import TestContext
from testData.models.view_models import LoginVM, UpdateUserVM
from appDriver import HttpClientOWF
from testData.scenarios.update_user_scenario import SUCCESS_UPDATE_SCENARIO


@pytest.mark.incremental
@pytest.mark.usefixtures('seed_users_before_scenario',
                         'seed_addresses_before_scenario',
                         'seed_passports_before_scenario',
                         'http_client')
class TestUpdateUser:
    context = TestContext()

    def test_login(self, http_client: HttpClientOWF):
        data_for_login: LoginVM = LoginVM.parse_obj(SUCCESS_UPDATE_SCENARIO.get('data_for_login'))
        response: requests.Response = http_client.login(data_for_login)
        self.context.add('accessToken', response.json()['accessToken'])

    def test_update_user(self, http_client: HttpClientOWF):
        """
        Не работает конвертация даты из json в datatime объект
        """
        data_for_update_user: UpdateUserVM = UpdateUserVM.parse_obj(SUCCESS_UPDATE_SCENARIO.get('data_for_update_user'))
        token = self.context.get('accessToken')
        response: requests.Response = http_client.update_user_requisites(token, data_for_update_user)
        assert response.status_code == 200, "Код ответа в методе обновления юзера не равен 200"

    def test_get_user_requisites(self, http_client: HttpClientOWF, snapshot):
        token = self.context.get('accessToken')
        response: requests.Response = http_client.get_user_requisites(token)
        try:
            content = response.json()
        except:
            assert False, "Реквизиты пользователя не удалось преобразовать в json"
        # paths позволяет игнорировать поля при добавлении в снапшот
        assert content == snapshot(exclude=paths("address.id", "passport.id"))
