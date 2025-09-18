def filter_by_state(lst: list, state: str = "EXECUTED") -> list:
    """Функция отбора по ключу state"""
    new_list = [i for i in lst if i.get("state") == state]
    return new_list


def sort_by_date(lst: list, key_sort: bool = True) -> list:
    """Функция сортировки даты"""
    new_list = sorted(lst, key=lambda x: x.get("date"), reverse=key_sort)
    return new_list
