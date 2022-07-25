from psycopg2 import Error
from psycopg2.extras import RealDictCursor


class DBClient:
    """
    Клиент для рабоыт с БД.
    connection описан в staticmethod connection
    """

    def __init__(self, connection):
        self.connection = connection

    def get_users(self) -> list:
        """
        Получение всех пользователей
        :return: возвращает список всех пользователей в базе
        """
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * from users")
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
