import pytest

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
        response = http_client.login(data_for_login)
        self.context.add('accessToken', response.json()['accessToken'])

    def test_update_user(self, http_client: HttpClientOWF):
        """
        На данный момент не работает преобразование в UpdateUserVM, проблема именно с АДресом и Паспортом
        я так подозреваю, что он не может преобразовать данные в модельку внутри другой модельки.
        Нужно либо их франкинштейнить, чего я делать не хочу или искать решение потипу енамок, указать
        class Config:
              use_enum_values = True
        """
        data_for_update_user: UpdateUserVM = UpdateUserVM.parse_obj(SUCCESS_UPDATE_SCENARIO.get('data_for_update_user'))
        token = self.context.get('accessToken')
        response = http_client.update_user_requisites(token, data_for_update_user)
        print('\n', response.status_code, '\n', response.json())
