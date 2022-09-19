import pytest

from testData.enums.imageFormats import ImageFormat
from testData.scenarios.add_avatar_scenarios import SUCCESS_SCENARIO, TEST_FILES_PATH
from testLogic.assertion_object import AssertionObject

@pytest.mark.incremental
@pytest.mark.usefixtures('seed_users_before_scenario',
                         'http_client',
                         'token')
class TestAddAvatar:
    """
    Тест дергает метод загрузки аватара, проверяет статус код
    """
    def test_add_avatar(self, http_client, token: str):
        # TODO> Мне не нравится то как оформлен путь, но как в json хранить путь до файла не привязываясь к операционке - я хз
        with open(TEST_FILES_PATH / SUCCESS_SCENARIO.get('file_name'), 'rb') as file:
            response = http_client.loads_avatar(token, file)

        print(response.text)

        assert response.status_code == 200, f"Код ответа не равен 200"

@pytest.mark.incremental
@pytest.mark.usefixtures('seed_users_before_scenario',
                         'http_client',
                         'token')
class TestGetAvatar:
    """
    Тест дергает метод получения аватара, проверяет статус код и формат полученого файла
    """
    def test_get_avatar(self, http_client, token):
        response = http_client.get_avatar(token)
        content = response.content
        assert response.status_code == 200, f"Код ответа не равен 200"
        assert AssertionObject.check_image_format(content, ImageFormat.JPEG), f'Проверяемый файл не PNG формата'
