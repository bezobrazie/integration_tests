class DBQueryHandler:
    """
    Класс в котором обрабатываются данные вытащенные из БД
    db_client - экземпляр класса с запросами к БД инициализируется в фикстурах конфтеста вместе с конекшеном.
    """

    def __init__(self, db_client):
        self.db_client = db_client

    def user_exist_check(self, email: str) -> bool:
        """
        :param email: строчное значение почты по которой мы ищем пользователя в базе
        :return: возвращает будевое значение True - пользователь есть в БД, False - пользователь отсутствует в БД
        """
        users_for_assert = []
        users = self.db_client.get_users()
        for user in users:
            users_for_assert.append(user.get('email'))
        if email in users_for_assert:
            return True
        else:
            return False