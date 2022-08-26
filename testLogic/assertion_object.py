from datetime import datetime, timedelta

from testData.models.db_models import User
import jwt


class AssertionObject:

    @staticmethod
    def user_exist_check(users: list[User], email: str) -> bool:
        """
        Проверка наличия пользователя в БД.
        :param email: строчное значение почты по которой мы ищем пользователя в базе
        :param users: список словарей с классами модели User
        :return: возвращает булевое значение.
        True - пользователь есть в БД, False - пользователь отсутствует в БД
        """
        users_for_assert = []
        for user in users:
            users_for_assert.append(user.email)
        if email in users_for_assert:
            return True
        else:
            return False

    @staticmethod
    def assertion_token_expire_one_hour(token: str) -> bool:
        """
        Вычисляет время жизни токена и проверяет, истекает ли он через час.
        :param token: токен
        """
        decode = jwt.decode(token, options={"verify_signature": False})

        exp_unix = decode['exp']
        exp_time = datetime.fromtimestamp(exp_unix)

        time_first = datetime.now() + timedelta(minutes=59)
        time_second = datetime.now() + timedelta(hours=1)

        if time_first < exp_time < time_second:
            return True
        else:
            return False
