from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
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
    creation_date: datetime
    update_date: datetime


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
    lockout_end: Optional[datetime]
    lockout_enabled: bool
    access_failed_count: int


class Address(BaseModel):
    """
    Модель представления данных из таблицы addresses
    """
    id: UUID
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
    user_id: UUID


class Passport(BaseModel):
    """
    Модель представления данных из таблицы passports
    """
    id: UUID
    series: str
    number: str
    department_code:  str
    birth_date: datetime
    issue_date: datetime
    birth_place: str
    issuer: str
    user_id: UUID


class Account(BaseModel):
    """
    Модель представления данных из таблицы accounts
    """
    id: UUID
    number: int
    type: AccountType
    state: int
    amount: int
    creation_date: datetime
    update_date: datetime
    user_id: UUID
