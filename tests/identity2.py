import pytest
from testData.identity_data import IdentityData

from appDriver import HttpClientOWF


# Файлик для теста identity2 (При создании  тестов как методов а не классов, удаление пользователя фикстурой - работает)
@pytest.mark.usefixtures('http_client', 'delete_user')
class TestFailedAutorization:
    """
    Авторизация с некорректными данными
    """

    @pytest.mark.parametrize(argnames="test_data",
                             argvalues=IdentityData.DATA_FOR_BAD_AUTH,
                             ids=[cases['case_name'] for cases in IdentityData.DATA_FOR_BAD_AUTH])
    @pytest.mark.usefixtures('http_client', 'delete_user')
    def test_register(self, http_client: HttpClientOWF, test_data):
        """
        Регистрация пользователя
        """
        response = http_client.register(IdentityData.VALID_REGISTRATION_DATA)
        print(response.json())

        assert response.status_code == 200, f'Статус код = {response.status_code}, должен быть 200'

        input = test_data["input"]
        response = http_client.login(input)

        assert response.status_code == 400, f'Статус код = {response.status_code}, должен быть 400'
        assert response.json().get('errorMessage') == test_data["expected"],\
            f"Сообщение {response.json().get('errorMessage')} не равно ожидаемому f\"Пользователь с email {input['email']} не найден\""
