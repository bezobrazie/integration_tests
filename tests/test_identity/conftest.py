import pytest

from appDriver import DBClient
from testData import IdentityData
from testData.models.view_models import RegisterVM


@pytest.fixture(scope="class")
def delete_user_class(db_connection):
    """
    Фикстура для удаления пользователя после тестирвоания.\
    """
    db_client = DBClient(db_connection)
    yield
    date_for_delete: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get("valid_data")
    db_client.delete_user(date_for_delete.email)


@pytest.fixture(scope="function")
def delete_user_func(db_connection):
    """
    Фикстура для удаления пользователя после тестирвоания, .
    """
    db_client = DBClient(db_connection)
    yield
    date_for_delete: RegisterVM = IdentityData.VALID_REGISTRATION_DATA.get("valid_data")
    db_client.delete_user(date_for_delete.email)