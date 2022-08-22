from typing import List
from uuid import UUID

from psycopg2.extras import RealDictCursor

from appDriver.dbDriver.db_query_variables import DBQueryVariables
from testData.models.db_models import User, Account


class DBClient:
    """
    Клиент для работы с БД.
    connection - функция def connect() из общего conftest
    """

    def __init__(self, connection):
        self.__connection = connection

    def get_users(self) -> list[User]:
        """
        Получение всех пользователей
        :return: возвращает список всех пользователей в базе
        """
        with self.__connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(DBQueryVariables.SELECT_ALL_USERS_QUERY)
            list_from_query = cursor.fetchall()
            user_list = []
            for user in list_from_query:
                user_list.append(User.parse_obj(user))
            return user_list

    def get_account_by_id(self, account_id: UUID) -> Account:
        """
        Получение счета из таблицы accounts по идентификатору счета
        :param account_id: IDшник счета который мы хотим получить
        :return: возвращает модельку счета
        """
        with self.__connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(DBQueryVariables.SELECT_ACCOUNT_BY_ID(account_id))

            accounts_from_query = cursor.fetchone()
            return Account.parse_obj(accounts_from_query)

    def get_accounts_by_ids(self, accounts_ids: List[UUID]) -> List[Account]:
        """
        Получение счета из таблицы accounts по идентификатору счета
        :param accounts_ids: список ID счетов которые мы хотим получить
        :return: возвращает список моделек счета
        """
        account_list = []

        for id in accounts_ids:
            account = self.get_account_by_id(id)
            account_list.append(account)

        return account_list
