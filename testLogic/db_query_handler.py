class DBQueryHandler:
    """
    Класс в котором обрабатываются данные вытащенные из БД
    db_client - экземпляр класса с запросами к БД инициализируется в фикстурах конфтеста вместе с конекшеном.
    """

    def user_exist_check(self, users: list, email: str) -> bool:
        """
        Проверка наличия пользователя в БД.
        :param email: строчное значение почты по которой мы ищем пользователя в базе
        :param users: список словарей с пользователями
        :return: возвращает будевое значение True - пользователь есть в БД, False - пользователь отсутствует в БД
        """
        users_for_assert = []
        for user in users:
            users_for_assert.append(user.get('email'))
        if email in users_for_assert:
            return True
        else:
            return False
