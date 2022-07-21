from testData.identity_data import IdentityData
import pytest


@pytest.mark.usefixtures('db_client', 'http_client')
class TestRegistration:

    @classmethod
    def setup_class(cls):
        cls.users_for_assert = []

    def test_find_user_before_registration(self, db_client):
        users = db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert IdentityData.TEST_DATA['email'] not in self.users_for_assert, f"Пользователь с почтой - {IdentityData.TEST_DATA['email']}, уже есть в БД"

    def test_register(self, http_client):
        response = http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 200

    def test_re_register(self, http_client):
        response = http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Пользователь с Email: post@mail.ru уже зарегистрирован"

    def test_find_user_after_registration(self, db_client):
        users = db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert IdentityData.TEST_DATA['email'] in self.users_for_assert

    #TODO - незнаю как запихнуть такой метод в тирдаун.
    def test_delete_user_after_test(self, db_client):
        db_client.delete_user(IdentityData.TEST_DATA['email'])

    @classmethod
    def teardown_class(cls, db_client):
        cls.db_client.delete_user(IdentityData.TEST_DATA['email'])


@pytest.mark.usefixtures('db_client', 'http_client')
class TestSuccessAutorization:

    def test_register(self, http_client):
        response = http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 200

    def setup(self):
        self.login_data = {
            'email': IdentityData.TEST_DATA['email'],
            'password': IdentityData.TEST_DATA['password']
        }

    def test_login(self, http_client):
        response = http_client.login(self.login_data)
        assert response.status_code == 200

    def test_delete_user_after_test(self, db_client):
        db_client.delete_user(IdentityData.TEST_DATA['email'])


@pytest.mark.usefixtures('db_client', 'http_client')
class TestFailedAutorizationBadLogin:

    def test_register(self, http_client):
        response = http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 200

    def test_login(self, http_client):
        response = http_client.login(IdentityData.FAILED_LOGIN_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Пользователь с email post@mail1.ru не найден"

    def test_delete_user_after_test(self, db_client):
        db_client.delete_user(IdentityData.TEST_DATA['email'])


@pytest.mark.usefixtures('db_client', 'http_client')
class TestFailedAutorizationBadPassword:

    def test_register(self, http_client):
        response = http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 200

    def test_login(self, http_client):
        response = http_client.login(IdentityData.FAILED_PASSWORD_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Неверный пароль"

    def test_delete_user_after_test(self, db_client):
        db_client.delete_user(IdentityData.TEST_DATA['email'])
