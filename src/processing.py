def filter_by_state(lst: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает state опционально и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению.
    """
    new_list = [i for i in lst if i.get("state") == state]
    return new_list


def sort_by_date(lst: list, key_sort: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр
    и возвращает новый список, отсортированный по дате (date).
    """
    new_list = sorted(lst, key=lambda x: x.get("date"), reverse=key_sort)
    return new_list
