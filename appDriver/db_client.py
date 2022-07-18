import psycopg2
from config import DB_CONCTIONS_PARAMS


class CreateConection:

    @staticmethod
    def create_OWF_DB_conection():
        return psycopg2.connect(
            dbname=DB_CONCTIONS_PARAMS.get('dbname'),
            user=DB_CONCTIONS_PARAMS.get('user'),
            password=DB_CONCTIONS_PARAMS.get('password'),
            host=DB_CONCTIONS_PARAMS.get('host'))


class DBClient:
    def __init__(self, conection):
        self.conection = conection

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