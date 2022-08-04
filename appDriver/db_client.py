from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from psycopg2.sql import SQL
from typing import Callable
from testLogic.db_query_handler import DBQueryHandler

class DBClient:
    """
    Клиент для рабоыт с БД.
    connection описан в staticmethod connection
    """

    __SELECT_ALL_USERS_QUERY = SQL("SELECT * FROM users;")

    # TODO: Нужно вынести эту функцию в отдельный файлик с query переменными и положить его в метод по удалению пользователя по почте.
    __DELETE_USER_BY_EMAIL_QUERY: Callable[[str], str] = lambda email: f"delete from \"AspNetUsers\" where user_name = '{email}'"

    def __init__(self, connection):
        self.connection = connection

    # TODO нужно возвращать список юзеров датакласами
    def get_users(self) -> list:
        """
        Получение всех пользователей
        :return: возвращает список всех пользователей в базе
        """
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(self.__SELECT_ALL_USERS_QUERY)
            return cursor.fetchall()

    def delete_user(self, email: str):
        """
        Удаление пользователя по email
        :param email: почта пользователя которого хотите удалить из базы
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"delete from \"AspNetUsers\" where user_name = '{email}'")
                self.connection.commit()
                count = cursor.rowcount
                print(count, f"Пользователь {email} успешно удален")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
