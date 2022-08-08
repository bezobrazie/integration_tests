from psycopg2 import Error
from psycopg2.extras import RealDictCursor

from appDriver.db_query_variables import DBQueryVariables


class DBClient:
    """
    Клиент для работы с БД.
    connection описан в staticmethod connection
    """

    def __init__(self, connection):
        self.connection = connection

    # TODO нужно возвращать список юзеров датакласами
    def get_users(self) -> list:
        """
        Получение всех пользователей
        :return: возвращает список всех пользователей в базе
        """
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(DBQueryVariables.SELECT_ALL_USERS_QUERY)
            return cursor.fetchall()

    def delete_user(self, email: str):
        """
        Удаление пользователя по email
        :param email: почта пользователя которого хотите удалить из базы
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(DBQueryVariables.DELETE_USER_BY_EMAIL_QUERY(email))
                self.connection.commit()
                count = cursor.rowcount
                print(count, f"Пользователь {email} успешно удален")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
