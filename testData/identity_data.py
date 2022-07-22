class IdentityData:
    """
    Класс хранения данных для тестирования
    """

    # Данные используемые для успешной решистрации
    VALID_REGISTRATION_DATA = {
        "email": "post@mail.ru",
        "password": "Test123456",
        "confirmPassword": "Test123456",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+79657020827"
    }

    # Данные используемые для успешной решистрации
    BAD_CONFIRM_PASSWORD_REGISTRATION_DATA = {
        "email": "post@mail.ru",
        "password": "Test123456",
        "confirmPassword": "Test1234567",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+79657020827"
    }

    BAD_EMAIL_REGISTRATION_DATA = {
        "email": "postmail.ru",
        "password": "Test123456",
        "confirmPassword": "Test123456",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+79657020827"
    }

    BAD_PHONE_REGISTRATION_DATE = {
        "email": "post@mail.ru",
        "password": "Test123456",
        "confirmPassword": "Test123456",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+49657020827"
    }

    # Данные испрользуемые в тестах по авторизации с некорректным логином.
    BAD_LOGIN = {
        "email": "post@mail1.ru",
        "password": "Test123456"
    }

    # Данные испрользуемые в тестах по авторизации с некорректным паролем.
    BAD_PASSWORD = {
        "email": "post@mail.ru",
        "password": "Test12345"
    }

    # Данные испрользуемые в тестах по успешной авторизации.
    VALID_AUTORIZATION = {
        "email": "post@mail.ru",
        "password": "Test123456"
    }

    DATA_FOR_BAD_REG = [
        (BAD_CONFIRM_PASSWORD_REGISTRATION_DATA, "Пароли не совпадают"),
        (BAD_EMAIL_REGISTRATION_DATA, "Электронный адрес должен соответствовать регулярному выражению ^[-\\w.]+@([A-z0-9][-A-z0-9]+\\.)+[A-z]{2,}$"),
        (BAD_PHONE_REGISTRATION_DATE, "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$"),
    ]