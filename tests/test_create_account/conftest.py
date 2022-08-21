import pytest

from appDriver.dbDriver.db_seeder import DBSeeder
from appDriver.dbDriver.db_cleaner import DBCleaner
from testData.scenarios.create_account_scenario import INITIAL_DATA
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction


# TODO: продумать обработку ошибок при попытке добавления записи, которая уже добавлена
@pytest.fixture(scope='session')
def seed_users_before_scenario(db_connection):
    """
    Фикстура для заполнения таблиц перед тестами, и чистки после тестов
    :param db_connection: psycopg2.connect объект коннекта к базе данных, нужен для инициализации классов для работы с БД
    """
    db_cleaner = DBCleaner(db_connection)
    db_seeder = DBSeeder(db_connection)
    try:
        db_seeder.seed_users(INITIAL_DATA['users'])
    except (InFailedSqlTransaction, UniqueViolation):
        tables = ['\"AspNetUsers\"']
        db_cleaner.clean_tables(tables)
        db_seeder.seed_users(INITIAL_DATA['users'])
    yield
    tables = ['\"AspNetUsers\"']
    db_cleaner.clean_tables(tables)


@pytest.fixture(scope='session')
def seed_addresses_before_scenario(db_connection):
    """
    Фикстура для заполнения таблицы адресс перед тестами, и чистки после тестов
    :param db_connection: psycopg2.connect объект коннекта к базе данных, нужен для инициализации классов для работы с БД
    """
    db_cleaner = DBCleaner(db_connection)
    db_seeder = DBSeeder(db_connection)
    db_seeder.seed_addresses(INITIAL_DATA['addresses'])
    yield
    tables = ["addresses"]
    db_cleaner.clean_tables(tables)


@pytest.fixture(scope='session')
def seed_passports_before_scenario(db_connection):
    """
    Фикстура для заполнения таблицы паспорт перед тестами, и чистки после тестов
    :param db_connection: psycopg2.connect объект коннекта к базе данных, нужен для инициализации классов для работы с БД
    """
    db_cleaner = DBCleaner(db_connection)
    db_seeder = DBSeeder(db_connection)
    db_seeder.seed_passport(INITIAL_DATA['passports'])
    yield
    tables = ["passports"]
    db_cleaner.clean_tables(tables)
