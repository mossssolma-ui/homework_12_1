from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной "currency"
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str | None, Any, None]:
    """
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction.get("description")