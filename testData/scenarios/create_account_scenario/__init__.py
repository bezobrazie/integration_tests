import os
from datetime import datetime
from uuid import UUID

from config import TEST_DATA_DIR
from testData import TestContext
from testData.models.db_models import User, IdentityUser, Address, Passport

from testData.models.view_models import CreateAccountVM

# Путь до папки с тестовыми данными
TEST_DATA_PATH = os.path.join(TEST_DATA_DIR, "scenarios", "create_account_scenario")

SUCCESS_SCENARIO = [
    TestContext.from_json_file(os.path.join(TEST_DATA_PATH, "scenario_1.json")),
    TestContext.from_json_file(os.path.join(TEST_DATA_PATH, "scenario_2.json")),
    TestContext.from_json_file(os.path.join(TEST_DATA_PATH, "scenario_3.json"))
]

WITHOUT_PERSONAL_DATA_SCENARIO = TestContext.from_json_file(os.path.join(TEST_DATA_PATH, "scenario_1.json"))

# Данные используются в DBSeeder для подготовки базы к тестам.
INITIAL_DATA = {
    'users': [
        (
            User.parse_obj({
                'id': UUID('e42557a0-cfb2-4a1e-a23d-274f4f86ea39'),
                'user_id': UUID('e42557a0-cfb2-4a1e-a23d-274f4f86ea39'),
                'first_name': 'Борис',
                'last_name': 'Ельцын',
                'patronymic': 'Тестович',
                'email': 'post@mail.ru',
                'phone_number': '+79657020827',
                'creation_date': datetime(2022, 2, 8),
                'update_date': datetime(2022, 5, 8)}
            ),
            IdentityUser.parse_obj({
                'id': UUID('e42557a0-cfb2-4a1e-a23d-274f4f86ea39'),
                'user_name': 'post@mail.ru',
                'normalized_user_name': 'POST@MAIL.RU',
                'email': 'post@mail.ru',
                'normalized_email': 'POST@MAIL.RU',
                'email_confirmed': True,
                'password_hash': 'AQAAAAEAACcQAAAAEMne2G6qVyLlXh6nZa6V6af+l//DYmfZGhrkWYATJMh1rhMMppk7H/62L3qxjxyR6A==',
                'security_stamp': 'A4OD2WRRTATJR3V3IJFONBYQBB24KGVJ',
                'concurrency_stamp': '03271595-75f6-4f13-8619-9ef80c4a1eb3',
                'phone_number_confirmed': True,
                'two_factor_enabled': True,
                'lockout_end': datetime(2022, 5, 7),
                'lockout_enabled': False,
                'access_failed_count': 2})
        )
    ],
    'addresses': [
        (
            Address.parse_obj({
                'id': UUID('07ecf4e0-f28c-4ae5-9f1b-c9bab785a1b9'),
                'post_index': 248195,
                'region_code': 40,
                'region_name': 'Калужская область',
                'area': "Ареа",
                'city': "Калуга",
                'locality': "Локалити",
                'street': "Пушкина",
                'house': "2",
                'housing': "2/2",
                'apartment': "15",
                'user_id': UUID('e42557a0-cfb2-4a1e-a23d-274f4f86ea39')})
        )
    ],
    'passports': [
        (
            Passport.parse_obj(
                {
                    'id': 'ff7fb4af-793d-43ad-b1cf-8bddc1336fa5',
                    'series': '2345',
                    'number': '234445',
                    'department_code': '666-666',
                    'birth_date': datetime(1994, 12, 16),
                    'issue_date': datetime(2015, 8, 15),
                    'birth_place': 'Сочи',
                    'issuer': 'Ишюер',
                    'user_id': UUID('e42557a0-cfb2-4a1e-a23d-274f4f86ea39')
                }
            )
        )
    ]

}
