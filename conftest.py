import pytest

from appDriver.http_client import HttpClientOWF
from config import BASE_URL_OFL
from appDriver.db_client import DBClient
from testData.identity_data import IdentityData


@pytest.fixture(scope="session")
def db_client():
    """
    Создает экземпляр класса DBClient - клиент для работы с БД вместе с конекшеном, в тирдауне закрывает конекшн.
    """
    connection = DBClient.connection()
    yield DBClient(connection)
    connection.close()


@pytest.fixture(scope="session")
def http_client():
    """
    Создает экземпляр класса HttpClientOWF - клиент для работы с HTTP запросами
    """
    return HttpClientOWF(BASE_URL_OFL)


@pytest.fixture(scope="class")
def user():
    '''
    Пробовал использовать данную фикстуру в тестах.
    В setup cоздает пользователя на основе заготовленого словаря, в тир даун этого пользователя удаляет.
    На данный момен нигде не используется. Можно его превратить в метод регистрации пользователя, тогда от него будет толк.
    '''
    connection = DBClient.connection()
    USER = IdentityData.VALID_REGISTRATION_DATA
    yield USER
    DBClient(connection).delete_user(USER['email'])
    connection.close()


#TODO можно запихнуть фикстуру в фикстуру, попробовать засунуть db-client сюда
@pytest.fixture(scope="class")
def delete_user():
    """
    Фикстура для удаления пользователя после тестирвоания.\
    """
    connection = DBClient.connection()
    yield
    DBClient(connection).delete_user(IdentityData.VALID_REGISTRATION_DATA['email'])
    connection.close()
