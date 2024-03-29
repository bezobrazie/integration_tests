import pytest

from testData import IdentityData
from testData import TestContext
from appDriver import DBClient, HttpClientOWF
from testLogic import AssertionObject
from testData.models.view_models import RegisterVM, LoginVM
from testData.models.parametrize_models import ParametrizeModel
from testData.models.db_models import User


# TODO>
#   Тест на регистрацию с пустыми полями
#   Тест на авторизацию с пустыми полями
#   Тест на авторизацию с невалидными полями (параметризованый)


@pytest.mark.incremental
@pytest.mark.usefixtures('db_connection', 'http_client', 'delete_user_class', 'db_client')
class TestSuccessRegistration:
    """
    Тест-кейс на регистрацию. Проверяет: регистрацию и повторную регистрацию.
    """

    def test_register(self, http_client: HttpClientOWF):
        """
        Регистрация пользователя
        """
        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        response = http_client.register(valid_data)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_re_register(self, http_client: HttpClientOWF):
        """
        Повторная регистрация пользователя
        """
        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        response = http_client.register(valid_data)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с Email: {valid_data.email} уже зарегистрирован",\
            f"Пользователь с Email: {valid_data.email} успешно повторно зарегистрировался"

    def test_find_user_after_registration(self, db_client: DBClient ):
        """
        Проверка наличия пользователя в БД. После регистрации, пользователь должен быть в БД.
        """

        users: list[User] = db_client.get_users()

        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        assert AssertionObject.user_exist_check(users, valid_data.email),\
            f"Пользователь с почтой - {valid_data.email}, отсутствует в БД"


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=IdentityData.DATA_FOR_BAD_REG,
                         scope="class",
                         ids=[cases.get("case").case_name for cases in IdentityData.DATA_FOR_BAD_REG])
@pytest.mark.usefixtures('db_connection', 'http_client', 'db_client')
class TestBadDataRegistration:
    """
    Параметризованный тест с ошибочными данными при регистрации.
    """

    def test_register(self, http_client: HttpClientOWF, test_data: TestContext):
        """
        Регистрация пользователя
        """
        date_for_test: ParametrizeModel = test_data.get("case")
        response = http_client.register(date_for_test.input)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        error_message = response.json().get('errorMessage')
        assert error_message == date_for_test.expected, f"В ответе от сервера сообщение об ошибке {error_message}, отличается от ожидаемого {date_for_test.expected}"

    @pytest.mark.usefixtures('delete_user_func')
    def test_find_user_after_registration(self, test_data: TestContext, db_client: DBClient):
        """
        Проверка на отсутствие пользователя в БД.
        """
        date_for_test: ParametrizeModel = test_data.get("case")
        test_input: RegisterVM = date_for_test.input

        users = db_client.get_users()

        assert not AssertionObject.user_exist_check(users, test_input.email),\
            f"Пользователь с почтой - {test_input.email} должен отсутствовать в БД. А он есть!! ;c"


@pytest.mark.incremental
@pytest.mark.usefixtures('http_client', 'delete_user_class')
class TestSuccessAutorization:
    """
    Тест на успешную авторизацию.
    """

    def test_register(self, http_client: HttpClientOWF):
        """
        Регистрация пользователя
        """
        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        response = http_client.register(valid_data)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client: HttpClientOWF):
        """
        Авторизация с валидными данными
        """
        data_for_login: LoginVM = IdentityData.AUTORIZATION_DATA.get("valid_data")
        response = http_client.login(data_for_login)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=IdentityData.DATA_FOR_BAD_AUTH,
                         scope="class",
                         ids=[cases.get('case').case_name for cases in IdentityData.DATA_FOR_BAD_AUTH])
@pytest.mark.usefixtures('http_client')
class TestFailedAutorization:
    """
    Авторизация с некорректными данными
    """

    def test_register(self, http_client: HttpClientOWF, test_data):
        """
        Регистрация пользователя
        """
        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        response = http_client.register(valid_data)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    @pytest.mark.usefixtures('delete_user_func')
    def test_login(self, http_client: HttpClientOWF, test_data: TestContext):
        """
        Авторизация с невалидным логином
        """
        date_for_test: ParametrizeModel = test_data.get("case")
        response = http_client.login(date_for_test.input)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == date_for_test.expected,\
            f"Сообщение {response.json().get('errorMessage')} не равно ожидаемому \"Пользователь с email {date_for_test.input.email} не найден\""


@pytest.mark.incremental
@pytest.mark.usefixtures('seed_users_before_scenario')
class TestTokenTimeOut:
    """
    Проверка токена на его время жизни
    """
    # создаем экземпляр контекста для передачи данных между шагами теста
    context = TestContext()

    def test_get_token(self, http_client: HttpClientOWF):
        """Получаем токен перед тестированием и передаем его в контекст"""
        data_for_login: LoginVM = IdentityData.AUTORIZATION_DATA.get("valid_data")

        response_json = http_client.login(data_for_login).json()
        token = response_json['accessToken']
        self.context.add('accessToken', token)

    def test_check_time_out_token(self):
        token = self.context.get('accessToken')
        assert AssertionObject.assertion_token_expire_one_hour(token),\
            "Срок через который истекает токен не равен 1 часу."
