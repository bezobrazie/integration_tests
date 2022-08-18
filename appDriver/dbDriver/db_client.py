from psycopg2 import Error
from psycopg2.extras import RealDictCursor

from appDriver.dbDriver.db_query_variables import DBQueryVariables
from testData.models.db_models import User


class DBClient:
    """
    Клиент для работы с БД.
    connection - функция def connect() из общего conftest

    """

    def __init__(self, connection):
        self.connection = connection

    def get_users(self) -> list[User]:
        """
        Получение всех пользователей
        :return: возвращает список всех пользователей в базе
        """
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(DBQueryVariables.SELECT_ALL_USERS_QUERY)
            list_from_query = cursor.fetchall()
            user_list = []
            for user in list_from_query:
                user_list.append(User.parse_obj(user))
            return user_list

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
