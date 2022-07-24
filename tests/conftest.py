import pytest
from testData.identity_data import IdentityData


# Файлик для теста identity2 (При создании  тестов как методов а не классов, удаление пользователя фикстурой - работает)
@pytest.fixture(scope="function", autouse=True)
def delete_user_func(db_client):
    """
    Фикстура для удаления пользователя после тестирвоания.\
    """
    yield
    db_client.delete_user(IdentityData.VALID_REGISTRATION_DATA['email'])