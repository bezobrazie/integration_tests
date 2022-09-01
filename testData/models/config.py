from humps import camelize
from pydantic import BaseModel


def to_camel_case(string: str):
    return camelize(string)


class CamelBaseModel(BaseModel):
    """Базовый класс, в потомках которого поля будут сериализоваться в camelCase"""

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
