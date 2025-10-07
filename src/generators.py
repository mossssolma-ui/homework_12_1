from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной "currency"
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "name" in transaction["operationAmount"]["currency"]
            and transaction["operationAmount"]["currency"]["name"] == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str | None, Any, None]:
    """
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """
    Функция генерации номеров банковских карт в диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения.
    """
    card_number = "0" * 16
    for num in range(start, end + 1):
        if start >= 1 and end <= 9999999999999999:
            card_number = card_number[: -len(str(num))] + str(num)
            card_number_format = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
            yield card_number_format
