from testData import TestContext
from testData.models.view_models import RegisterVM, LoginVM
from testData.models.parametrize_models import ParametrizeModel


class IdentityData:
    """
    Класс хранения данных для тестирования
    """

    # Данные используемые в тестах по регистрации с некорректным подтверждением пароля.
    INVALID_REGISTRATION_DATA = TestContext.from_dict(
        {
            "bad_confirm_password": RegisterVM.parse_obj({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test1234567",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            "bad_email": RegisterVM.parse_obj({
                "email": "postmail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            "bad_phone": RegisterVM.parse_obj({
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
            'valid_data': RegisterVM.parse_obj({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "patronymic": "Тестович",
                "phoneNumber": "+79657020827"}),
            'valid_data_without_patronymic': RegisterVM.parse_obj({
                "email": "post@mail.ru",
                "password": "Test123456",
                "confirmPassword": "Test123456",
                "firstName": "Борис",
                "lastName": "Ельцын",
                "phoneNumber": "+79657020827"})
        })

    # Данные для авторизации валидные/невалидные
    AUTORIZATION_DATA = TestContext.from_dict({
        "valid_data": LoginVM.parse_obj({
            "email": "post@mail.ru",
            "password": "Test123456"}),
        "bad_login": LoginVM.parse_obj({
            "email": "post@mail1.ru",
            "password": "Test123456"}),
        "bad_password": LoginVM.parse_obj({
            "email": "post@mail.ru",
            "password": "Test12345"})
    })

    # Данные используемые в параметризации для негативных тестов регистрации
    DATA_FOR_BAD_REG = [
        TestContext.from_dict({
            "case": ParametrizeModel.parse_obj({
                "input": INVALID_REGISTRATION_DATA.get("bad_confirm_password"),
                "expected": "Пароли не совпадают",
                "case_name": "Registering with mismatched passwords"})}),
        TestContext.from_dict({
            "case": ParametrizeModel.parse_obj({
                "input": INVALID_REGISTRATION_DATA.get("bad_email"),
                "expected": "Электронный адрес должен соответствовать регулярному выражению ^[-\\w.]+@([A-z0-9][-A-z0-9]+\\.)+[A-z]{2,}$",
                "case_name": "Email does not pass regular expression"})}),
        TestContext.from_dict({
            "case": ParametrizeModel.parse_obj({
                "input": INVALID_REGISTRATION_DATA.get("bad_phone"),
                "expected": "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$",
                "case_name": "Phone number doesn't pass regular expression"})})]

    # Данные используемые в параметризации для негативных тестов авторизации, обернуты в контекст
    DATA_FOR_BAD_AUTH = [
        TestContext.from_dict({
            'case': ParametrizeModel.parse_obj({
                "input": AUTORIZATION_DATA.get("bad_login"),
                "expected": f"Пользователь с email {AUTORIZATION_DATA.get('bad_login').email} не найден",
                "case_name": "Login with incorrect login"})}),
        TestContext.from_dict({
            'case': ParametrizeModel.parse_obj({
                "input": AUTORIZATION_DATA.get("bad_password"),
                "expected": "Неверный пароль",
                "case_name": "Login with incorrect password"})})]
