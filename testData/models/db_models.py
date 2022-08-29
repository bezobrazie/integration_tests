from uuid import UUID
from typing import Optional
from datetime import date

from pydantic import BaseModel, UUID4
from testData.enums.account_type import AccountType


# TODO: информация об опциональности полей не актуальна
class User(BaseModel):
    """
    Модель представления данных из таблицы users
    """
    id: UUID
    user_id: UUID
    first_name: str
    last_name: str
    patronymic: Optional[str]
    email: str
    phone_number: str
    photo_file_id: Optional[UUID]
    creation_date: date
    update_date: date


class IdentityUser(BaseModel):
    """
    Модель представления данных из таблицы AspNetUsers
    """
    id: UUID
    user_name: str
    normalized_user_name: str
    email: str
    normalized_email: str
    email_confirmed: bool
    password_hash: str
    security_stamp: str
    concurrency_stamp: str
    phone_number: Optional[str]
    phone_number_confirmed: bool
    two_factor_enabled: bool
    lockout_end: Optional[date]
    lockout_enabled: bool
    access_failed_count: int


class Address(BaseModel):
    """
    Модель представления данных из таблицы addresses
    """
    id: UUID4 | None
    post_index: int
    region_code: int
    region_name: str
    area: str
    city: str
    locality: str
    street: str
    house: str
    housing: str
    apartment: str
    user_id: UUID4 | None


class Passport(BaseModel):
    """
    Модель представления данных из таблицы passports
    """
    id: UUID4 | None
    series: str
    number: str
    department_code:  str
    birth_date: date
    issue_date: date
    birth_place: str
    issuer: str
    user_id: UUID4 | None


class Account(BaseModel):
    """
    Модель представления данных из таблицы accounts
    """
    id: UUID
    number: int
    type: AccountType
    state: int
    amount: int
    creation_date: date
    update_date: date
    user_id: UUID
