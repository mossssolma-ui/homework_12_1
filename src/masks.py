def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки банковской карты.
    Принимает на вход номер карты и возвращает ее маску
    """
    my_card_number = str(card_number)
    if len(my_card_number) >= 16:
        card_text = my_card_number[:6] + "*" * (len(my_card_number) - 10) + my_card_number[-4:]
        result = " ".join([card_text[i : i + 4] for i in range(0, len(card_text), 4)])
    else:
        result = my_card_number
    return result


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки банковского счета.
    Принимает на вход номер счета и возвращает его маску.
    """
    if not isinstance(account_number, int):
        raise TypeError("Номер счета должен быть целым числом")
    account_number_str = str(account_number)
    if len(account_number_str) >= 5:
        result = "**" + account_number_str[-4:]
    else:
        result = account_number_str
    return result
