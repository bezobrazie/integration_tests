import pytest

from appDriver.dbDriver.db_seeder import DBSeeder
from appDriver.dbDriver.db_cleaner import DBCleaner
from testData.scenarios.update_user_scenario import INITIAL_DATA


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
def seed_addresses_before_scenario(db_cleaner: DBCleaner, db_seeder: DBSeeder):
    """
    Фикстура для заполнения таблицы адресс перед тестами, и чистки после тестов
    :param db_cleaner: экземпляр класса  DBCleaner, инициализируется в фикстуре в общем конфтесте.
    :param db_seeder: экземпляр класса  DBSeeder, инициализируется в фикстуре в общем конфтесте.
    """
    db_seeder.seed_addresses(INITIAL_DATA['addresses'])
    yield
    tables = ["addresses"]
    db_cleaner.clean_tables(tables)


@pytest.fixture(scope='class')
def seed_passports_before_scenario(db_cleaner: DBCleaner, db_seeder: DBSeeder):
    """
    Фикстура для заполнения таблицы паспорт перед тестами, и чистки после тестов
    :param db_cleaner: экземпляр класса  DBCleaner, инициализируется в фикстуре в общем конфтесте.
    :param db_seeder: экземпляр класса  DBSeeder, инициализируется в фикстуре в общем конфтесте.
    """
    db_seeder.seed_passport(INITIAL_DATA['passports'])
    yield
    tables = ["passports"]
    db_cleaner.clean_tables(tables)
