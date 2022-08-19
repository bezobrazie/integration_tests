import pytest

from appDriver.dbDriver.db_seeder import DBSeeder
from appDriver.dbDriver.db_cleaner import DBCleaner
from testData.scenarios.create_account_scenario import INITIAL_DATA


@pytest.fixture(scope='session')
def seed_data_before_scenario(db_connection):
    """
    Фикстура для заполнения таблиц перед тестами, и чистки после тестов
    :param db_connection: psycopg2.connect объект коннекта к базе данных, нужен для инициализации классов для работы с БД
    """
    db_seeder = DBSeeder(db_connection)
    db_cleaner = DBCleaner(db_connection)
    db_seeder.seed_users(INITIAL_DATA['users'])
    yield
    tables = ["users", '\"AspNetUsers\"']
    db_cleaner.clean_tables(tables)
