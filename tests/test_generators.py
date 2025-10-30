import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

TRANSACTIONS = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 4,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EURO", "code": "EURO"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
]


@pytest.mark.parametrize(
    "transact, currency, expected",
    [
        # проверка по заданной валюте, USD
        (
            TRANSACTIONS,
            "USD",
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 3,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
        ),
        # проверка, когда поле валюты пустое
        (TRANSACTIONS, "", []),
        # проверка, когда валюта отсутствует
        (TRANSACTIONS, "MARK", []),
        # проверка, когда входной список пуст
        ([], "USD", []),
    ],
)
def test_filter_by_currency(transact, currency, expected):
    """
    Тест транзакций:
    по заданной валюте,
    по пустому полю currency,
    когда указана несуществующая валюта,
    когда входной список пуст
    """
    result = list(filter_by_currency(transact, currency))
    assert result == expected


def test_transaction_descriptions_fixt(valid_transaction):
    assert list(transaction_descriptions([TRANSACTIONS[0]])) == [valid_transaction]


def test_transaction_descriptions():
    """
    Тест описания транзакций
    """
    transaction_descript = list(transaction_descriptions(TRANSACTIONS))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert transaction_descript == expected


@pytest.mark.parametrize(
    "transact, expected",
    [
        ([], []),
        (
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Перевод организации"],
        ),
        (
            TRANSACTIONS,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
    ],
)
def test_transaction_descriptions_(transact, expected):
    """
    Проверка различных входных транзакций, включая пустой список
    """
    assert list(transaction_descriptions(transact)) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # проверка генерации 2-ух номеров карт
        (
            1,
            2,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
            ],
        ),
        # проверка генерации нескольких номеров карт
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        # проверка генерации минимального номера карты
        (
            1,
            1,
            [
                "0000 0000 0000 0001",
            ],
        ),
        # проверка генерации максимального номера карты
        (
            9999999999999999,
            9999999999999999,
            [
                "9999 9999 9999 9999",
            ],
        ),
        # проверка если start > end
        (5, 1, []),
    ],
)
def test_card_number_generator(start, end, expected):
    """
    Проверка номеров:
    проверка генерации 2-ух номеров карт,
    проверка генерации нескольких номеров карт,
    проверка генерации минимального номера карты,
    проверка генерации максимального номера карты,
    проверка если start > end
    """
    assert list(card_number_generator(start, end)) == expected
