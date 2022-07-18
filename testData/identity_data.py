
class IdentityData:

  TEST_DATA = {
    "email": "post@mail.ru",
    "password": "Test123456",
    "confirmPassword": "Test123456",
    "firstName": "Борис",
    "lastName": "Ельцын",
    "patronymic": "Тестович",
    "phoneNumber": "+79657020827"
  }

  FAILED_LOGIN_DATA = {
    "email": "post@mail1.ru",
    "password": "Test123456"
  }

  FAILED_PASSWORD_DATA = {
    "email": "post@mail.ru",
    "password": "Test12345"
  }
