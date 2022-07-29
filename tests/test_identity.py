import pytest
from testData import IdentityData
from testData import TestContext
from testLogic.db_query_handler import DBQueryHandler
from appDriver import DBClient
from appDriver import HttpClientOWF
from testData.models.view_models import RegisterVM, LoginVM

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
        assert response.json().get('errorMessage') == f"Пользователь с Email: {IdentityData.VALID_REGISTRATION_DATA.get('valid_data').email} уже зарегистрирован",\
            f"Пользователь с Email: {valid_data.email} успешно повторно зарегистрировался"

    def test_find_user_after_registration(self, db_client: DBClient):
        """
        Проверка наличия пользователя в БД. После регистрации, пользователь должен быть в БД.
        """
        users = db_client.get_users()
        valid_data: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get('valid_data')
        assert DBQueryHandler().user_exist_check(users, valid_data.email),\
            f"Пользователь с почтой - {IdentityData.VALID_REGISTRATION_DATA.get('email')}, отсутствует в БД"


@pytest.mark.incremental
@pytest.mark.parametrize(argnames="test_data",
                         argvalues=IdentityData.DATA_FOR_BAD_REG,
                         scope="class",
                         ids=[cases.get("case_name") for cases in IdentityData.DATA_FOR_BAD_REG])
@pytest.mark.usefixtures('db_client', 'http_client')
class TestBadDataRegistration:
    """
    Параметризованный тест с ошибочными данными при регистрации.
    """

    def test_register(self, http_client: HttpClientOWF, test_data: TestContext):
        """
        Регистрация пользователя
        """
        response = http_client.register(test_data.get("input"))

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        error_message = response.json().get('errorMessage')
        assert error_message == test_data.get("expected"), f"В ответе от сервера сообщение об ошибке {error_message}, отличается от ожидаемого {test_data.get('expected')}"

    @pytest.mark.usefixtures('delete_user_func')
    def test_find_user_after_registration(self, db_client: DBClient, test_data: TestContext):
        """
        Проверка на отсутствие  пользователя в БД.
        """
        test_input = test_data.get("input")
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
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA.get_dict())

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client: HttpClientOWF):
        """
        Авторизация с валидными данными
        """
        response = http_client.login({"email": IdentityData.VALID_REGISTRATION_DATA.get("email"),
                                      "password": IdentityData.VALID_REGISTRATION_DATA.get("password")})

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
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA.get_dict())
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
