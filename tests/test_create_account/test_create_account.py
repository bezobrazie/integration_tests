import pytest

from appDriver import HttpClientOWF, DBClient
from testData import TestContext
from testData.models.view_models import CreateAccountVM, LoginVM
from testData.models.db_models import Account
from testData.enums.account_type import AccountType
from testData.scenarios.create_account_scenario import SUCCESS_SCENARIO, WITHOUT_PERSONAL_DATA_SCENARIO


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=SUCCESS_SCENARIO,
                         scope="class",
                         ids=[cases.get('name_case') for cases in SUCCESS_SCENARIO])
@pytest.mark.usefixtures('seed_users_before_scenario',
                         'seed_addresses_before_scenario',
                         'seed_passports_before_scenario',
                         'http_client',
                         'db_client')
class TestCreateAccount:
    # создаем экземпляр контекста для передачи данных между шагами теста
    context = TestContext()

    def test_get_token(self, http_client: HttpClientOWF, test_data: TestContext):
        """Получаем токен перед тестированием и передаем его в контекст"""
        data_for_login: LoginVM = LoginVM.parse_obj(test_data.get('data_for_login'))

        response_json = http_client.login(data_for_login).json()
        token = response_json['accessToken']
        self.context.add('accessToken', token)

    def test_create_account(self, http_client: HttpClientOWF, test_data: TestContext):
        """Попытка создания аккаунта"""
        data_for_create_account: CreateAccountVM = CreateAccountVM.parse_obj(test_data.get('account'))
        token = self.context.get('accessToken')

        response = http_client.create_account(token, data_for_create_account)

        response_json = response.json()
        account_id = response_json['accountId']
        self.context.add('accountId', account_id)

        assert response.status_code == 200, f"Статус ответа равен {response.status_code}, ожидалось 200"

    def test_asserts(self, test_data: TestContext, db_client: DBClient):
        """Проверки"""
        account_id = self.context.get('accountId')
        account: Account = db_client.get_account_with_id(account_id)
        assert account.type == AccountType.SAVING
        # совпадение user_id
        # проверка на значение в поле amount == 500,3
        # проверка на state == 1 сделать Enum
        # проверка на время


@pytest.mark.incremental
@pytest.mark.usefixtures('seed_users_before_scenario', 'http_client')
class TestCreateAccountWithoutPersonalData:
    """
    Тест на проверку эксепшена в случае регистрации без заполнения персональных данных.
    """
    # создаем экземпляр контекста для передачи данных между шагами теста
    context = TestContext()

    def test_get_token(self, http_client: HttpClientOWF):
        """Получаем токен перед тестированием и передаем его в контекст"""
        data_for_login: LoginVM = LoginVM.parse_obj(WITHOUT_PERSONAL_DATA_SCENARIO.get('data_for_login'))

        response_json = http_client.login(data_for_login).json()
        token = response_json['accessToken']
        self.context.add('accessToken', token)

    def test_create_account(self, http_client: HttpClientOWF):
        """Попытка создания аккаунта"""
        data_for_create_account: CreateAccountVM = CreateAccountVM.parse_obj(WITHOUT_PERSONAL_DATA_SCENARIO.get('account'))
        token = self.context.get('accessToken')

        response = http_client.create_account(token, data_for_create_account)
        # добавить проверка на отсутствие аккаунта в базе, возможно вынести ассерты в отдельный метод
        assert response.status_code == 400, f"Статус ответа равен {response.status_code}, ожидалось 400"
        assert response.json().get('errorMessage') == f"Перед созданием счёта необходимо заполнить личные данные"
