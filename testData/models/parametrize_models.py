from typing import Any
from pydantic import BaseModel


class ParametrizeModel(BaseModel):
    """ Модель данных для использования параметризации в тестах"""
    input: Any
    expected: str
    case_name: str
