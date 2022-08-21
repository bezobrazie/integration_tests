from datetime import datetime
from typing import Any, List, Tuple

from testData.models.db_models import User, IdentityUser, Address, Passport
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

    def seed_addresses(self, addresses: List[Tuple[Address]]):
        """
        Метод который добавляет в таблицу addresses запись
        :param addresses: кортеж с адресами, которые нужно записать в базу
        """
        insert_addresses_query = DBQueryVariables.INSERT_ADDRESS_QUERY

        for address in addresses:
            insert_addresses_query += self.unpack_to_tuple(address) + ',\n'

        insert_addresses_query = insert_addresses_query[:-2]

        with self.__connection.cursor() as cursor:
            cursor.execute(insert_addresses_query)
            self.__connection.commit()

    def seed_passport(self, passports: List[Tuple[Passport]]):
        """
        Метод который добавляет в таблицу passports запись
        :param passports: кортеж с паспортными данными, которые нужно записать в базу
        """
        insert_passports_query = DBQueryVariables.INSERT_PASSPORTS_QUERY

        for passport in passports:
            insert_passports_query += self.unpack_to_tuple(passport) + ',\n'

        insert_passports_query = insert_passports_query[:-2]

        with self.__connection.cursor() as cursor:
            cursor.execute(insert_passports_query)
            self.__connection.commit()

    @staticmethod
    def unpack_to_tuple(model: Any) -> str:
        """
        :param model: модель которую необходимо распаковать и превратить в Tuple
        :return: строку, отформатированную для записи в БД.
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
