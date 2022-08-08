from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """
    Модель представления данных из таблицы users
    """
    id: UUID
    first_name: str
    last_name: str
    patronymic: Optional[str]
    email: str
    phone_number: str
    creation_date: datetime
    update_date: datetime
