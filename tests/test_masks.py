import pytest
from src.masks import get_mask_card_number, get_mask_account


# фикстура и параметризованный тест для функции get_mask_card_number
def test_get_mask_card_number(card_number):
    assert get_mask_card_number(1596837868705199) == card_number


@pytest.mark.parametrize("card_number, expected", [
    (0, "0"),
    (1, "1"),
    (1234567, "1234567"),
    (123456789012345, "123456789012345"),
    (1234567890123456, "1234 56** **** 3456"),
    (12345678901234567, "1234 56** **** *456 7"),
    (123456789012345678, "1234 56** **** **56 78"),
    (1234567890123456789, "1234 56** **** ***6 789"),
    (12345678901234567890, "1234 56** **** **** 7890"),
])
def test_get_mask_card_number_different_length(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# фикстура и параметризированный тест для функции get_mask_account
def test_get_mask_account(number_valid):
    assert get_mask_account(1234567890) == number_valid


@pytest.mark.parametrize("number_valid, expected", [
    (1, "1"),
    (12, "12"),
    (123, "123"),
    (1234, "1234"),
    (12345, "**2345"),
    (1234567890, "**7890"),
    (12345678901234567, "**4567"),
    (1234567, "**4567"),
])
def test_get_mask_account_different_length(number_valid, expected):
    assert get_mask_account(number_valid) == expected


def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account("123")
    with pytest.raises(TypeError):
        get_mask_account(None)
