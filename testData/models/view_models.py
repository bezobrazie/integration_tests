from typing import Optional

from pydantic import BaseModel, UUID4

from testData.enums.account_type import AccountType
from testData.models.db_models import Address, Passport


class RegisterVM(BaseModel):
    """ Модель представления данных для регистрации """
    email: str
    password: str
    confirmPassword: str
    firstName: str
    lastName: str
    patronymic: Optional[str]
    phoneNumber: str


class LoginVM(BaseModel):
    """ Модель представления данных для авторизации """
    email: str
    password: str


class CreateAccountVM(BaseModel):
    """ Модель представления данных для создания счета """
    type: AccountType

    # Первоначальный взнос.
    amount: float

    class Config:
        use_enum_values = True


class UpdateUserVM(BaseModel):
    id: UUID4
    firstName: str
    lastName: str
    patronymic: str
    phoneNumber: str
    address: Address
    passport: Passport
