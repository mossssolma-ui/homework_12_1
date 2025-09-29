import pytest


# module masks.py
@pytest.fixture
def card_number():
    return "1596 83** **** 5199"


@pytest.fixture
def number_valid():
    return "**7890"


# module widget.py
@pytest.fixture
def card_valid():
    return "Maestro 1596 83** **** 5199"


@pytest.fixture
def account_valid():
    return "Счет **9589"


@pytest.fixture
def valid_date():
    return "11.03.2024"