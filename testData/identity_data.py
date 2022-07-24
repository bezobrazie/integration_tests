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

    # Данные используемые в тестах по регистрации с некорректным подтверждением пароля.
    BAD_CONFIRM_PASSWORD_REGISTRATION_DATA = {
        "email": "post@mail.ru",
        "password": "Test123456",
        "confirmPassword": "Test1234567",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+79657020827"
    }

    # Данные используемые в тестах по регистрации с некорректным логином.
    BAD_EMAIL_REGISTRATION_DATA = {
        "email": "postmail.ru",
        "password": "Test123456",
        "confirmPassword": "Test123456",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+79657020827"
    }

    # Данные используемые в тестах по авторизации с некорректным телефоном.
    BAD_PHONE_REGISTRATION_DATE = {
        "email": "post@mail.ru",
        "password": "Test123456",
        "confirmPassword": "Test123456",
        "firstName": "Борис",
        "lastName": "Ельцын",
        "patronymic": "Тестович",
        "phoneNumber": "+49657020827"
    }

    # Данные используемые в тестах по авторизации с некорректным логином.
    BAD_LOGIN = {
        "email": "post@mail1.ru",
        "password": "Test123456"
    }

    # Данные используемые в тестах по авторизации с некорректным паролем.
    BAD_PASSWORD = {
        "email": "post@mail.ru",
        "password": "Test12345"
    }

    # Данные используемые в тестах по успешной авторизации.
    VALID_AUTORIZATION = {
        "email": "post@mail.ru",
        "password": "Test123456"
    }

    # Данные используемые в параметризации для негативных тестов регистрации
    DATA_FOR_BAD_REG = [
        {"input": BAD_CONFIRM_PASSWORD_REGISTRATION_DATA,
         "expected": "Пароли не совпадают",
         "case_name": "Registering with mismatched passwords"},
        {"input": BAD_EMAIL_REGISTRATION_DATA,
         "expected": "Электронный адрес должен соответствовать регулярному выражению ^[-\\w.]+@([A-z0-9][-A-z0-9]+\\.)+[A-z]{2,}$",
         "case_name": "Email does not pass regular expression"},
        {"input": BAD_PHONE_REGISTRATION_DATE,
         "expected": "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$",
         "case_name": "Phone number doesn't pass regular expression"}
    ]

    # Данные используемые в параметризации для негативных тестов авторизации
    DATA_FOR_BAD_AUTH = [
        {"input": BAD_LOGIN,
         "expected": f"Пользователь с email {BAD_LOGIN['email']} не найден",
         "case_name": "Login with incorrect login"},
        {"input": BAD_PASSWORD,
         "expected": "Неверный пароль",
         "case_name": "Login with incorrect password"}
    ]