
class EndpointVariables:
    """
    Класс для хранения переменных используемых как роуты в HTTP запросах.
    """
    # путь для метода используемого для регистрации
    REGISTER_ROUTE = "api/auth/register"

    # путь для метода используемого для авторизации
    LOGIN_ROUTE = "api/auth/login"

    # путь для метода используемого для создания нового счета
    CREATE_ACCOUNT_ROUTE = "api/accounts/create"

    # путь для метода используемого для обновления пользователя
    UPDATE_USER = 'api/user/requisites/update'

    # путь для метода на получение реквизитов
    GET_REQUISITES = 'api/user/requisites'
