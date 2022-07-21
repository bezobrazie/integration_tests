class IdentityData:

  VALID_REGISTRATION_DATA = {
    "email": "post@mail.ru",
    "password": "Test123456",
    "confirmPassword": "Test123456",
    "firstName": "Борис",
    "lastName": "Ельцын",
    "patronymic": "Тестович",
    "phoneNumber": "+79657020827"
  }

  BAD_LOGIN = {
    "email": "post@mail1.ru",
    "password": "Test123456"
  }

  BAD_PASSWORD = {
    "email": "post@mail.ru",
    "password": "Test12345"
  }

  VALID_AUTORIZATION = {
    "email": "post@mail.ru",
    "password": "Test123456"
  }
