from config import BASE_URL_OFL, DB_CONCTIONS_PARAMS
from appDriver.http_client import HttpClientOWF
from appDriver.db_client import DBClient
from testData.identity_data import IdentityData


class TestRegistration:

    def setup(self):
        self.http_client = HttpClientOWF(BASE_URL_OFL)
        self.connection = DBClient.create_conection()
        self.db_client = DBClient(self.connection)
        self.users_for_assert = []

    def test_find_user_before_registration(self):
        users = self.db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert IdentityData.TEST_DATA['email'] not in self.users_for_assert, f"Пользователь с почтой - {IdentityData.TEST_DATA['email']}, уже есть в БД"

    def test_register(self):
        response = self.http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 200

    def test_re_register(self):
        response = self.http_client.register(IdentityData.TEST_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Пользователь с Email: post@mail.ru уже зарегистрирован"

    def test_find_user_after_registration(self):
        users = self.db_client.get_users()
        for user in users:
            self.users_for_assert.append(user.get('email'))

        assert IdentityData.TEST_DATA['email'] in self.users_for_assert

    def teardown(self):
        self.connection.close()
        #TODO чистить БД от пользователя


class TestSuccessAutorization:

    def setup(self):
        self.http_client = HttpClientOWF(BASE_URL_OFL)
        self.login_data = {
            'email': IdentityData.TEST_DATA['email'],
            'password': IdentityData.TEST_DATA['password']
        }

    def test_login(self):
        response = self.http_client.login(self.login_data)
        assert response.status_code == 200


class TestFailedAutorizationBadLogin:

    def setup(self):
        self.http_client = HttpClientOWF(BASE_URL_OFL)

    def test_login(self):
        response = self.http_client.login(IdentityData.FAILED_LOGIN_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Пользователь с email post@mail1.ru не найден"


class TestFailedAutorizationBadPassword:

    def setup(self):
        self.http_client = HttpClientOWF(BASE_URL_OFL)

    def test_login(self):
        response = self.http_client.login(IdentityData.FAILED_PASSWORD_DATA)
        assert response.status_code == 400
        assert response.json().get('errorMessage') == "Неверный пароль"
