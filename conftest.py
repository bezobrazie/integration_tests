import pytest
import psycopg2
from appDriver import HttpClientOWF
from appDriver import DBClient
from config import BASE_URL_OFL
from config import DB_CONCTIONS_PARAMS
from testData.identity_data import IdentityData
from collections import defaultdict


def connect() -> psycopg2.connect:
    """
    Функция возвращает объект коннекта. Конект к БД используется при создании класса DBClient в фикстуре db_client.
    """
    return psycopg2.connect(
        dbname=DB_CONCTIONS_PARAMS.get('dbname'),
        user=DB_CONCTIONS_PARAMS.get('user'),
        password=DB_CONCTIONS_PARAMS.get('password'),
        host=DB_CONCTIONS_PARAMS.get('host'))


@pytest.fixture(scope="session")
def db_client():
    """
    Создает экземпляр класса DBClient - клиент для работы с БД вместе с конекшеном, в тирдауне закрывает конекшн.
    """
    connection = connect()
    yield DBClient(connection)
    connection.close()


@pytest.fixture(scope="session")
def http_client():
    """
    Создает экземпляр класса HttpClientOWF - клиент для работы с HTTP запросами
    """
    return HttpClientOWF(BASE_URL_OFL)


@pytest.fixture(scope="class")
def delete_user_class(db_client):
    """
    Фикстура для удаления пользователя после тестирвоания.\
    """
    yield
    db_client.delete_user(IdentityData.VALID_REGISTRATION_DATA['email'])


@pytest.fixture(scope="function")
def delete_user_func(db_client):
    """
    Фикстура для удаления пользователя после тестирвоания, .
    """
    yield
    db_client.delete_user(IdentityData.VALID_REGISTRATION_DATA['email'])

# Код ниже отвечает за пропуск тестов(шагов) внутри одного класса, если хоть один из них упал. 
__TEST_FAILED_INCREMENTAL = defaultdict(dict)


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None and call.excinfo.typename != "Skipped":
            param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            __TEST_FAILED_INCREMENTAL[str(item.cls)].setdefault(param, item.originalname or item.name)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
        originalname = __TEST_FAILED_INCREMENTAL[str(item.cls)].get(param)
        if originalname:
            pytest.xfail("previous test failed ({})".format(originalname))
