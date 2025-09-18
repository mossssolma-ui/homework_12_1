def filter_by_state(lst: list, state: str = "EXECUTED") -> list:
    """Функция отбора по ключу state"""
    new_list = [i for i in lst if i.get("state") == state]
    return new_list
