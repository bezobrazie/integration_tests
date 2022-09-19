import pytest

from appDriver.dbDriver.db_seeder import DBSeeder
from appDriver.dbDriver.db_cleaner import DBCleaner
from appDriver import HttpClientOWF
from testData.models.view_models import LoginVM
from testData.scenarios.add_avatar_scenarios import INITIAL_DATA, LOGIN_DATA


@pytest.fixture(scope='class', autouse=True)
def clean_data_base_before_scenario(db_cleaner: DBCleaner):
    """
    Фикстура для очистки базы данных до начала тестирования
    :param db_cleaner: экземпляр класса  DBCleaner, инициализируется в фикстуре в общем конфтесте.
    """
    tables = ['\"AspNetUsers\"']
    db_cleaner.clean_tables(tables)


@pytest.fixture(scope='class')
def seed_users_before_scenario(db_cleaner: DBCleaner, db_seeder: DBSeeder):
    """
    Фикстура для заполнения таблиц перед тестами, и чистки после тестов
    :param db_cleaner: экземпляр класса  DBCleaner, инициализируется в фикстуре в общем конфтесте.
    :param db_seeder: экземпляр класса  DBSeeder, инициализируется в фикстуре в общем конфтесте.
    """
    db_seeder.seed_users(INITIAL_DATA['users'])
    yield
    tables = ['\"AspNetUsers\"']
    db_cleaner.clean_tables(tables)


@pytest.fixture(scope='class')
def token(http_client: HttpClientOWF):
    data_for_login: LoginVM = LoginVM.parse_obj(LOGIN_DATA)

    response= http_client.login(data_for_login)

    if response.status_code == 200:
        return response.json()['accessToken']

    raise Exception('Не удалось авторизоваться и получить токен')
