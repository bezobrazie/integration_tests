from typing import Optional
from pydantic import BaseModel


class RegisterVM(BaseModel):
    """ Модель представления данных для регистрации"""
    email: str
    password: str
    confirmPassword: str
    firstName: str
    lastName: str
    patronymic: Optional[str]
    phoneNumber: str


class LoginVM(BaseModel):
    """ Модель представления данных для авторизации"""
    email: str
    password: str
