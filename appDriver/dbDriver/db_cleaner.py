from psycopg2 import Error

from appDriver.dbDriver.db_query_variables import DBQueryVariables


class DBCleaner:
    """
    Класс с методами по чистке БД
    """

    def __init__(self, connection):
        self.__connection = connection

    def clean_tables2(self, tables: list) -> None:
        """
        Метод для очистки таблицы.
        :param tables: список таблиц которые нужно очистить
        """
        for table in tables:
            query = DBQueryVariables.DELETE_TABLE_QUERY(table)
            try:
                with self.__connection.cursor() as cursor:
                    cursor.execute(query)
                    self.__connection.commit()
                    print(f"Таблица {table} успешно очищена")
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)

    def clean_tables(self, tables: list) -> None:
        """
        Метод для очистки таблицы.
        :param tables: список таблиц которые нужно очистить
        """
        try:
            with self.__connection.cursor() as cursor:
                for table in tables:
                    query = DBQueryVariables.DELETE_TABLE_QUERY(table)
                    cursor.execute(query)
                self.__connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def delete_user(self, email: str):
        """
        Удаление пользователя по email
        :param email: почта пользователя которого хотите удалить из базы
        """
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(DBQueryVariables.DELETE_USER_BY_EMAIL_QUERY(email))
                self.__connection.commit()
                count = cursor.rowcount
                print(count, f"Пользователь {email} успешно удален")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
