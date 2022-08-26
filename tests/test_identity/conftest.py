import pytest

from appDriver import DBCleaner
from appDriver import DBSeeder
from testData import IdentityData
from testData.models.view_models import RegisterVM
from testData.scenarios.identity_scenarios import INITIAL_DATA


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


@pytest.fixture(scope="class")
def delete_user_class(db_connection):
    """
    Фикстура для удаления пользователя после тестирвоания.\
    """
    db_client = DBCleaner(db_connection)
    yield
    date_for_delete: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get("valid_data")
    db_client.delete_user(date_for_delete.email)


@pytest.fixture(scope="function")
def delete_user_func(db_connection):
    """
    Фикстура для удаления пользователя после тестирвоания, .
    """
    db_client = DBCleaner(db_connection)
    yield
    date_for_delete: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get("valid_data")
    db_client.delete_user(date_for_delete.email)
