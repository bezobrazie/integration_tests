from psycopg2 import Error


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
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * from users")
            records = cursor.fetchall()

            users = list()
            for row in records:
                users.append(
                    {
                        "id": row[0],
                        "first_name": row[2],
                        "last_name": row[3],
                        "patronymic": row[4],
                        "email": row[5],
                        "phone_number": row[6]
                    }
                )

            return users

    def delete_user(self, email: str):
        """
        Удаление пользователя по email
        :param email: почта пользователя которого хотите удалить из базы
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"delete from users where email = '{email}'")
                cursor.execute(f"delete from \"AspNetUsers\" where user_name = '{email}'")
                self.connection.commit()
                count = cursor.rowcount
                print(count, "Запись успешно удалена")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
