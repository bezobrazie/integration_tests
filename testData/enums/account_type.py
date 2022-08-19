from enum import Enum


class AccountType(Enum):
    # Неизвестный тип
    UNKNOWN = 0
    # Накопительный счет
    SAVING = 1
    # быстрый счет
    EXPRESS = 2
    # кредитный счет
    CREDIT = 3
    # счет продавца
    TRADER = 4
