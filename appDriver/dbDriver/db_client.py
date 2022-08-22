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

    def get_account_with_id(self, account_id: UUID) -> Account:
        """
        Получение счета из таблицы accounts по идентификатору счета
        :param account_id: IDшник счета который мы хотим получить
        :return: возвращает модельку счета
        """
        with self.__connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(DBQueryVariables.SELECT_ACCOUNT_WITH_ID(account_id))
            accounts_from_query = cursor.fetchall()
            accounts_list = []
            for account in accounts_from_query:
                accounts_list.append(Account.parse_obj(account))
            return accounts_list[0]

    def get_accounts_with_ids(self, accounts_id: List[UUID]) -> List[Account]:
        """
        Получение счета из таблицы accounts по идентификатору счета
        :param accounts_id: список IDшников счетов которые мы хотим получить
        :return: возвращает список моделек счета
        """
        account_list = []
        for id in accounts_id:
            account = self.get_account_with_id(id)
            for element in account:
                account_list.append(element)

        return account_list
