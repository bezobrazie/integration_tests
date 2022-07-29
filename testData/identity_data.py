from testData import TestContext
from testData.models.view_models import RegisterVM, LoginVM


class IdentityData:
    """
    Класс хранения данных для тестирования
    """

    # Данные используемые в тестах по регистрации с некорректным подтверждением пароля.
    INVALID_REGISTRATION_DATA = TestContext.from_dict(
        {
            "bad_confirm_password": RegisterVM.from_dict({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test1234567",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            "bad_email": RegisterVM.from_dict({
                "email": "postmail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            "bad_phone": RegisterVM.from_dict({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+49657020827"})

        })

    # Данные используемые для успешной решистрации
    VALID_REGISTRATION_DATA = TestContext.from_dict(
        {
            'valid_data': RegisterVM.from_dict({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            'valid_data_without_patronymic': RegisterVM.from_dict({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": None,
                "phoneNumber": "+79657020827"})
    })

    # Данные используемые в тестах по авторизации с некорректным логином.
    BAD_LOGIN = LoginVM.from_dict({
        "email": "post@mail1.ru",
        "password": "Test123456"
    })

    # Данные используемые в тестах по авторизации с некорректным паролем.
    BAD_PASSWORD = LoginVM.from_dict({
        "email": "post@mail.ru",
        "password": "Test12345"
    })

    # Данные используемые в тестах по успешной авторизации.
    VALID_AUTORIZATION = TestContext.from_dict({
        "email": "post@mail.ru",
        "password": "Test123456"
    })

    # Данные используемые в параметризации для негативных тестов регистрации
    DATA_FOR_BAD_REG = [
        TestContext.from_dict({
         "input": INVALID_REGISTRATION_DATA.get("bad_confirm_password"),
         "expected": "Пароли не совпадают",
         "case_name": "Registering with mismatched passwords"}),
        TestContext.from_dict({
         "input": INVALID_REGISTRATION_DATA.get("bad_email"),
         "expected": "Электронный адрес должен соответствовать регулярному выражению ^[-\\w.]+@([A-z0-9][-A-z0-9]+\\.)+[A-z]{2,}$",
         "case_name": "Email does not pass regular expression"}),
        TestContext.from_dict({
          "input": INVALID_REGISTRATION_DATA.get("bad_phone"),
          "expected": "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$",
          "case_name": "Phone number doesn't pass regular expression"})
    ]

    # Данные используемые в параметризации для негативных тестов авторизации, обернуты в контекст
    DATA_FOR_BAD_AUTH = [
        TestContext.from_dict({
         "input": BAD_LOGIN,
         "expected": f"Пользователь с email {BAD_LOGIN.email} не найден",
         "case_name": "Login with incorrect login"}),
        TestContext.from_dict({
         "input": BAD_PASSWORD,
         "expected": "Неверный пароль",
         "case_name": "Login with incorrect password"})
    ]
