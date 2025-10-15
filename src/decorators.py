from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str | None) -> Callable[..., Any]:
    """
    Функция, которая возвращает декоратор,
    неоходим для логирования выполнения функции
    Если filename указан - логи выводим в файл,
    иначе - выводятся в консоль
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            message = ""
            try:
                start_func = time()
                result = func(*args, **kwargs)
                end_func = time()
                message = (
                    f"Функция {func.__name__} выполнилась. \n"
                    f"Время работы функции:\n"
                    f"старт: {start_func}\n"
                    f"окончание: {end_func}\n"
                    f"Время работы: {end_func - start_func:.3f}\n"
                    f"Результат: {result}\n\n"
                )
            except Exception as e:
                message = f"Функция {func.__name__} error: {e}. Входные данные args: {args}, kwargs: {kwargs}\n\n"
                raise

            finally:
                if filename:
                    with open(filename, "a", encoding="utf8") as file:
                        file.write(message)
                else:
                    print(message)
            return result

        return wrapper

    return decorator
