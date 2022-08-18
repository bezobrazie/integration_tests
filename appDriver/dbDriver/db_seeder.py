from datetime import datetime
from typing import Any, List, Tuple

from testData.models.db_models import User, IdentityUser
from appDriver.dbDriver.db_query_variables import DBQueryVariables


class DBSeeder:
    """
    Класс для заполнения БД данными перед тестами
    """

    def __init__(self, connection):
        self.__connection = connection

    def seed_users(self, users: List[Tuple[User, IdentityUser]]) -> None:
        """
        Метод который добавляет в таблицы AspNetUsers и users записи
        :param users: список кортежей в которых хранятся модели User и IdentityUser
        """
        insert_users_query = DBQueryVariables.INSERT_USER_QUERY
        insert_iusers_query = DBQueryVariables.INSERT_ASP_NET_USERS_QUERY

        for user, iuser in users:
            insert_users_query += self.unpack_to_tuple(user) + ',\n'
            insert_iusers_query += self.unpack_to_tuple(iuser) + ',\n'

        insert_users_query = insert_users_query[:-2]
        insert_iusers_query = insert_iusers_query[:-2]

        with self.__connection.cursor() as cursor:
            cursor.execute(insert_iusers_query)
            cursor.execute(insert_users_query)
            self.__connection.commit()

    @staticmethod
    def unpack_to_tuple(model: Any) -> str:
        """
        :param model: модель которую необходимо распаковать и превратить в тюпл
        :param users: список словарей с классами модели User
        :return: возвращает булевое значение.
        """
        temp = tuple()
        for field in model.__fields__:
            attr = getattr(model, field)
            if isinstance(attr, datetime):
                temp += (attr.isoformat(),)
            else:
                temp += (attr,)

        result = str(temp)
        result = result.replace("False", "false")
        result = result.replace("True", "true")
        result = result.replace("None", "null")
        return result
