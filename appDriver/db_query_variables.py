from typing import Callable

from psycopg2.sql import SQL


class DBQueryVariables:
    """
    Класс для хранения переменных в которых содержаться заготовленные запросы.
    """

    # запрос для выбора всех пользователей
    SELECT_ALL_USERS_QUERY = SQL("SELECT * FROM users;")

    # лямбда функция на получение запроса для удаления пользователя по email
    DELETE_USER_BY_EMAIL_QUERY: Callable[[str], str] = lambda email: f"delete from \"AspNetUsers\" where user_name = '{email}'"
