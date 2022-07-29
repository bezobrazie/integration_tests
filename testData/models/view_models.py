from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from typing import Optional


@dataclass
class RegisterVM(JSONWizard):
    """ Модель представления данных для регистрации"""
    email: str
    password: str
    confirmPassword: str
    firstName: str
    lastName: str
    patronymic: Optional[str]
    phoneNumber: str


@dataclass
class LoginVM(JSONWizard):
    email: str
    password: str
