def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки банковской карты.
    Принимает на вход номер карты и возвращает ее маску
    """
    card_text = str(card_number)[:6] + "*" * 6 + str(card_number)[12:]
    return " ".join([card_text[i : i + 4] for i in range(0, len(card_text), 4)])


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки банковского счета.
    Принимает на вход номер счета и возвращает его маску.
    """
    account_text = str(account_number)[-4:]
    return "**" + account_text
