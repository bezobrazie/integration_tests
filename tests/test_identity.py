import pytest
from testData.identity_data import IdentityData
from testLogic.db_query_handler import DBQueryHandler
from appDriver import DBClient
from appDriver import HttpClientOWF
from testData.context import TestContext

# TODO Тест на регистрацию с пустыми полями
# TODO Тест на авторизацию с пустыми полями
# TODO Тест на авторизацию с невалидными полями (параметризованый)
# TODO Тест на протухший токен


@pytest.mark.incremental
@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user_class')
class TestSuccessRegistration:
    """
    Тест-кейс на регистрацию. Проверяет: регистрацию и повторную регистрацию.
    """

    def test_register(self, http_client: HttpClientOWF):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_re_register(self, http_client: HttpClientOWF):
        """
        Повторная регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с Email: {IdentityData.VALID_REGISTRATION_DATA['email']} уже зарегистрирован",\
            f"Пользователь с Email: {IdentityData.VALID_REGISTRATION_DATA['email']} успешно повторно зарегистрировался"

    def test_find_user_after_registration(self, db_client: DBClient):
        """
        Проверка наличия пользователя в БД. После регистрации, пользователь должен быть в БД.
        """
        users = db_client.get_users()
        assert DBQueryHandler().user_exist_check(users, IdentityData.VALID_REGISTRATION_DATA['email']),\
            f"Пользователь с почтой - {IdentityData.VALID_REGISTRATION_DATA['email']}, отсутствует в БД"


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=IdentityData.DATA_FOR_BAD_REG,
                         scope="class",
                         ids=[cases['case_name'] for cases in IdentityData.DATA_FOR_BAD_REG])
@pytest.mark.usefixtures('db_client', 'http_client')
class TestBadDataRegistration:
    """
    Параметризованный тест с ошибочными данными при регистрации.
    """

    def test_register(self, http_client: HttpClientOWF, test_data: dict):
        """
        Регистрация пользователя
        """
        response = http_client.register(test_data["input"])

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        error_message = response.json().get('errorMessage')
        assert error_message == test_data["expected"], f"В ответе от сервера сообщение об ошибке {error_message}, отличается от ожидаемого {test_data['expected']}"

    @pytest.mark.usefixtures('delete_user_func')
    def test_find_user_after_registration(self, db_client: DBClient, test_data: dict):
        """
        Проверка на отсутствие  пользователя в БД.
        """
        test_input = test_data["input"]
        users = db_client.get_users()
        assert not DBQueryHandler().user_exist_check(users, test_input['email']),\
            f"Пользователь с почтой - {test_input['email']} должен отсутствовать в БД. А он есть!! ;c"


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
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client: HttpClientOWF):
        """
        Авторизация с валидными данными
        """
        response = http_client.login(IdentityData.VALID_AUTORIZATION)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=IdentityData.DATA_FOR_BAD_AUTH,
                         scope="class",
                         ids=[cases.get("case_name") for cases in IdentityData.DATA_FOR_BAD_AUTH])
@pytest.mark.usefixtures('http_client')
class TestFailedAutorization:
    """
    Авторизация с некорректными данными
    """

    def test_register(self, http_client: HttpClientOWF, test_data: TestContext):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)
        print(response.json())

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    @pytest.mark.usefixtures('delete_user_func')
    def test_login(self, http_client: HttpClientOWF, test_data: TestContext):
        """
        Авторизация с невалидным логином
        """
        input = test_data.get("input")
        response = http_client.login(input)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == test_data.get('expected'),\
            f"Сообщение {response.json().get('errorMessage')} не равно ожидаемому f\"Пользователь с email {input['email']} не найден\""
