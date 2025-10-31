import json

from .external_api import convert_to_rub


def load_financial_transactions(file_path: str) -> list[dict]:
    """
    Функция принимает JSON-файл в качестве аргумента
    и возвращает список словарей с данными о финансовых транзакциях.

    Если JSON-файл пустой, содержит не-список или не найден,
    возвращается пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            result = json.load(f)
            if isinstance(result, list):
                return result
            else:
                return []
    except FileNotFoundError as e:
        print(f"Файл не найден {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения файла {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях.
    Если транзакция была в USD или EUR, происходит вызов
    функции convert_to_rub, которая обращается к внешнему API
    """
    operation = transaction.get("operationAmount")

    if not isinstance(operation, dict):
        return 0.0

    amount = float(operation.get("amount", 0))

    cur = operation.get("currency")
    if isinstance(cur, dict):
        cur_code = cur.get("code")
    else:
        return 0.0

    if cur_code == "RUB":
        return amount
    elif cur_code in ["USD", "EUR"]:
        to_rub = convert_to_rub(amount, cur_code)
        return to_rub if to_rub else 0.0
    else:
        return 0.0
