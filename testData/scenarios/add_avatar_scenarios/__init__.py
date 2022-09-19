import os
from datetime import date
from uuid import UUID

from testData import TestContext
from testData.models.db_models import User, IdentityUser
from config import TEST_DATA_DIR

# Путь до папки с тестовыми данными
TEST_DATA_PATH = TEST_DATA_DIR / "scenarios" / "add_avatar_scenarios"
TEST_FILES_PATH = TEST_DATA_PATH / "data"

SUCCESS_SCENARIO = TestContext.from_json_file(TEST_DATA_PATH / "scenario_1.json")


LOGIN_DATA = {
    "email": "post@mail.ru",
    "password": "Test123456"
  }

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
                'photo_file_id': '231d21d5aa904db0b9b075fe71fbb9b8',
                'creation_date': date(2022, 2, 8),
                'update_date': date(2022, 5, 8)}
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
                'lockout_end': date(2022, 5, 7),
                'lockout_enabled': False,
                'access_failed_count': 2})
        )
    ]
}