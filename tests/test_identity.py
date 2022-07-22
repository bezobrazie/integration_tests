from testData.identity_data import IdentityData
import pytest

#TODO 'Электронный адрес должен соответствовать регулярному выражению ' '^[-\\w.]+@([A-z0-9][-A-z0-9]+\\.)+[A-z]{2,}$'
#TODO написать метод для проверки пользователя в БД
#TODO Тест на протухший токен
#TODO Посмотреть, какие ошибки выдает API http://localhost:8000/api-docs/index.html
#TODO Ввести параметризацию
#TODO Добавить коментарии и тайпхинты


@pytest.mark.usefixtures('db_client', 'http_client', 'user')
class TestRegistration:

    @classmethod
    def setup_class(cls):
        cls.users_for_assert = []

    def test_find_user_before_registration(self, db_client, user):
        users = db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert user['email'] not in self.users_for_assert, f"Пользователь с почтой - {user['email']}, уже есть в БД"

    def test_register(self, http_client, user):
        response = http_client.register(user)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_re_register(self, http_client, user):
        response = http_client.register(user)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с Email: {user['email']} уже зарегистрирован", f"Пользователь с Email: {user['email']} успешно повторно зарегистрировался"

    def test_find_user_after_registration(self, db_client, user):
        users = db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert user['email'] in self.users_for_assert, f"Пользователя {user['email']} отсутствует в БД"


@pytest.mark.usefixtures('db_client', 'http_client', 'user')
class TestSuccessAutorization:

    def test_register(self, http_client, user):
        response = http_client.register(user)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client, user):
        response = http_client.login(IdentityData.VALID_AUTORIZATION)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'


@pytest.mark.usefixtures('db_client', 'http_client', 'user')
class TestFailedAutorizationBadLogin:

    def test_register(self, http_client, user):
        response = http_client.register(user)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 400'

    def test_login(self, http_client):
        response = http_client.login(IdentityData.BAD_LOGIN)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == f"Пользователь с email {IdentityData.BAD_LOGIN['email']} не найден",\
            f"Сообщение {response.json().get('errorMessage')} не равно ожидаемому f\"Пользователь с email {IdentityData.BAD_LOGIN['email']} не найден\""


@pytest.mark.usefixtures('db_client', 'http_client', 'user')
class TestFailedAutorizationBadPassword:

    def test_register(self, http_client, user):
        response = http_client.register(user)

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

    def test_login(self, http_client):
        response = http_client.login(IdentityData.BAD_PASSWORD)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == "Неверный пароль",\
            f"Ошибка {response.json().get('errorMessage')} не равна ожидаемой \"Неверный пароль\""
