from testData.identity_data import IdentityData
from testLogic.db_query_handler import DBQueryHandler

import pytest

#TODO сделать нейминги для параметризованных тестов
#TODO Регистрация Пустые поля (параметризованный)

#TODO Авторизация пустые поля
#TODO Авторизация невалидные поля (параметризованый)

#TODO сделать наименования тестов.
#TODO Тест на протухший токен
#TODO Подумать, стоит ли выносить регистрацию пользователя в фикстуру, т.к. она используется почти в каждом тесте на identity


@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user')
class TestSuccessRegistration:
    """
    Тест-кейс на регистрацию. Проверяет: регистрацию и повторную регистрацию.
    """

    # TODO удалить проверку test_find_user_before_registration
    def test_find_user_before_registration(self, db_client):
        """
        Проверка наличия пользователя в БД. Перед регистрацией пользователя быть не должно.
        """
        #TODO Сделать внутри теста вызов get_users а затем передавать данные в метод логики
        assert not DBQueryHandler(db_client).user_exist_check(IdentityData.VALID_REGISTRATION_DATA['email']),\
            f"Пользователь с почтой - {IdentityData.VALID_REGISTRATION_DATA['email']}, уже есть в БД"

    def test_register(self, http_client):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_re_register(self, http_client):
        """
        Повторная регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с Email: {IdentityData.VALID_REGISTRATION_DATA['email']} уже зарегистрирован",\
            f"Пользователь с Email: {IdentityData.VALID_REGISTRATION_DATA['email']} успешно повторно зарегистрировался"

    def test_find_user_after_registration(self, db_client):
        """
        Проверка наличия пользователя в БД. После регистрации, пользователь должен быть в БД.
        """
        assert DBQueryHandler(db_client).user_exist_check(IdentityData.VALID_REGISTRATION_DATA['email']),\
            f"Пользователь с почтой - {IdentityData.VALID_REGISTRATION_DATA['email']}, отсутствует в БД"


@pytest.mark.parametrize("test_input,expected", IdentityData.DATA_FOR_BAD_REG)
@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user')
class TestBadDataRegistration:
    def test_find_user_before_registration(self, db_client, test_input, expected):
        """
        Проверка наличия пользователя в БД. Перед регистрацией пользователя быть не должно.
        """
        assert not DBQueryHandler(db_client).user_exist_check(test_input['email']),\
            f"Пользователь с почтой - {test_input['email']}, уже есть в БД"

    def test_register(self, http_client, test_input, expected):
        """
        Регистрация пользователя
        """
        response = http_client.register(test_input)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        error_message = response.json().get('errorMessage')
        assert error_message == expected, f"В ответе от сервера сообщение об ошибке {error_message}, отличается от ожидаемого {expected}"

    def test_find_user_after_registration(self, db_client, test_input, expected):
        """
        Проверка на отсутствие  пользователя в БД.
        """
        assert not DBQueryHandler(db_client).user_exist_check(test_input['email']),\
            f"Пользователь с почтой - {test_input['email']}, присутствует  в БД"


@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user')
class TestSuccessAutorization:
    """
    Тест на успешную авторизацию.
    """

    def test_register(self, http_client):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client):
        """
        Авторизация с валидными данными
        """
        response = http_client.login(IdentityData.VALID_AUTORIZATION)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'


@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user')
class TestFailedAutorizationBadLogin:
    """
    Авторизация с некоректным логином
    """

    def test_register(self, http_client):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client):
        """
        Авторизация с невалидным логином
        """
        response = http_client.login(IdentityData.BAD_LOGIN)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с email {IdentityData.BAD_LOGIN['email']} не найден",\
            f"Сообщение {response.json().get('errorMessage')} не равно ожидаемому f\"Пользователь с email {IdentityData.BAD_LOGIN['email']} не найден\""


@pytest.mark.usefixtures('db_client', 'http_client', 'delete_user')
class TestFailedAutorizationBadPassword:
    """
    Авторизация с некоректным паролем
    """

    def test_register(self, http_client, user):
        """
        Регистрация пользователя
        """
        response = http_client.register(user)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client):
        """
        Авторизация с невалидным паролем
        """
        response = http_client.login(IdentityData.BAD_PASSWORD)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == "Неверный пароль",\
            f"Ошибка {response.json().get('errorMessage')} не равна ожидаемой \"Неверный пароль\""
