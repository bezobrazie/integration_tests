from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from typing import Any


@dataclass
class ParametrizeModel(JSONWizard):
    """ Модель данных для использования параметризации в тестах"""
    input: Any
    expected: str
    case_name: str
