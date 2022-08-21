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

    # лямбда функция возвращает
    DELETE_TABLE_QUERY: Callable[[str], str] = lambda table: f"DELETE FROM {table};"

    # запрос на добавление пользователя в таблицу users
    INSERT_USER_QUERY = "INSERT INTO users VALUES\n"

    # запрос на добавление адреса в таблицу addresses
    INSERT_ADDRESS_QUERY = "INSERT INTO addresses VALUES\n"

    # запрос на добавление адреса в таблицу passports
    INSERT_PASSPORTS_QUERY = "INSERT INTO passports VALUES\n"

    # запрос на добавление пользователя в таблицу AspNetUsers
    INSERT_ASP_NET_USERS_QUERY = "INSERT INTO \"AspNetUsers\" VALUES\n"