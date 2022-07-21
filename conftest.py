import pytest

from appDriver.http_client import HttpClientOWF
from config import BASE_URL_OFL
from appDriver.db_client import DBClient
from testData.identity_data import IdentityData


@pytest.fixture(scope="session")
def db_client():
    connection = DBClient.connection()
    yield DBClient(connection)
    connection.close()


@pytest.fixture(scope="session")
def http_client():
    return HttpClientOWF(BASE_URL_OFL)


@pytest.fixture(scope="class")
def user():
    connection = DBClient.connection()
    USER = IdentityData.VALID_REGISTRATION_DATA
    yield USER
    DBClient(connection).delete_user(USER['email'])
    connection.close()
