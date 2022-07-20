import psycopg2
from config import DB_CONCTIONS_PARAMS
from psycopg2 import Error


class DBClient:
    def __init__(self, conection):
        self.conection = conection

    @staticmethod
    def create_conection():
        return psycopg2.connect(
            dbname=DB_CONCTIONS_PARAMS.get('dbname'),
            user=DB_CONCTIONS_PARAMS.get('user'),
            password=DB_CONCTIONS_PARAMS.get('password'),
            host=DB_CONCTIONS_PARAMS.get('host'))

    def get_users(self) -> list:
        """ Получение всех пользователей """
        with self.conection.cursor() as cursor:
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

    def delete_user(self, user: str):
        try:
            with self.conection.cursor() as cursor:
                cursor.execute(f"delete from users where email = '{user}'")
                cursor.execute(f"delete from \"AspNetUsers\" where user_name = '{user}'")
                self.conection.commit()
                count = cursor.rowcount
                print(count, "Запись успешно удалена")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    #TODO добавить метод для проверки существования пользователя
