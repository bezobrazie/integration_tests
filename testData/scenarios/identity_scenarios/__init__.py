from datetime import datetime
from uuid import UUID

from testData.models.db_models import User, IdentityUser


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
    ]
}
