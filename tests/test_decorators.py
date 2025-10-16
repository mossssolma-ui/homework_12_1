import pytest
from src.decorators import log


def test_log_console(capsys):
    """Функция выполнена. Вывод в консоль"""

    @log(filename=None)
    def add(x, y):
        return x + y

    res = add(5, 3)
    assert res == 8

    captured = capsys.readouterr()
    output = captured.out

    assert "Функция add выполнилась." in output
    assert "Результат: 8" in output
    assert "Время работы функции:" in output


def test_log_error_console(capsys):
    """Функция не выполнена. Вывод в консоль"""

    @log(filename=None)
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    output = captured.out

    assert "divide error:" in output
    assert "args: (10, 0)" in output
    assert "kwargs: {}" in output


def test_log():
    """Возврат исходного значения"""

    @log(filename=None)
    def identity(x):
        return x

    assert identity(15) == 15
    assert identity('test') == 'test'
    assert identity([1, 2, 3]) == [1, 2, 3]


def test_log_file_success(tmp_path):
    """Функция выполнена. Запись в файл"""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(3, 7)
    assert result == 21

    content = log_file.read_text(encoding="utf8")
    assert "Функция multiply выполнилась." in content
    assert "Результат: 21" in content
