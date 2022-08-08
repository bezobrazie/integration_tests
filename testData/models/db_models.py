from uuid import UUID
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class User(JSONWizard):
    id: UUID
    first_name: str
    last_name: str
    patronymic: Optional[str]
    email: str
    phone_number: str
    creation_date: datetime
    update_date: datetime
