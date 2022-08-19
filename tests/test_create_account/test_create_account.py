import os

import pytest

from testData.models.view_models import CreateAccountVM
from appDriver import HttpClientOWF
from testData.scenarios.create_account_scenario import SCENARIO_CONT
from config import TEST_DATA_DIR

# Путь до папки с тестовыми данными
TEST_DATA_PATH = os.path.join(TEST_DATA_DIR, "scenarios", "create_account_scenario")


@pytest.mark.incremental
@pytest.mark.usefixtures('seed_data_before_scenario', 'http_client')
def test_create_account(http_client: HttpClientOWF):
    # вначале логинимся и забираем из запроса токен
    # пишем токен в тест контекст и передаем его дальше
    data_for_create_account: CreateAccountVM = CreateAccountVM.parse_obj(SCENARIO_CONT.get('account'))
    response = http_client.create_account(data_for_create_account)
    print(response.text)
