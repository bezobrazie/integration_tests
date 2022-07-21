import pytest
from config import DB_CONCTIONS_PARAMS
import psycopg2
from appDriver.http_client import HttpClientOWF
from config import BASE_URL_OFL
from appDriver.db_client import DBClient


@pytest.fixture(scope="session")
def db_client():
    connection = psycopg2.connect(
        dbname=DB_CONCTIONS_PARAMS.get('dbname'),
        user=DB_CONCTIONS_PARAMS.get('user'),
        password=DB_CONCTIONS_PARAMS.get('password'),
        host=DB_CONCTIONS_PARAMS.get('host'))
    yield DBClient(connection)
    connection.close()


@pytest.fixture(scope="session")
def http_client():
    return HttpClientOWF(BASE_URL_OFL)
