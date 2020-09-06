from utils import draw_boxes


def divide(x: int, y: int) -> float:
    return x / y


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


def demo_raise_from(x: int, y: int):
    try:
        _ = divide(x, y)
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero") from e
    except TypeError:
        print("Invalid Datatype passed")
        raise


def demo_possibilities(x: int, y: int):
    try:
        _ = divide(x, y)
    except Exception:
        print("An Error Occured")
        print("Except Block: Runs when an exception occurs")
    else:
        print("Else Block: Runs only if NO exception occurs")
    finally:
        print("Finally Block: Always runs\n")


"""
Custom Exceptions
-----------------
Whenever possible make use of python defined exceptions. However, we can create our custom exception class very easily.
It is all about communication. If an error that could occur is not very well defined by python, create custom exceptions.
"""


class NegativeNumberException(Exception):
    pass


class FloatException(Exception):
    pass


def demo_custom_exceptions(num: int):
    if num < 0:
        raise NegativeNumberException("Negative number passed")
    elif type(num) == float:
        raise FloatException("Float value passed")
    else:
        print(f"Factorial({num} - {factorial(num)})")


if __name__ == "__main__":
    # draw_boxes('Demonstrating "raise from"')
    # demo_raise_from(2, 0)
    # demo_raise_from(2, "x")

    draw_boxes("Demonstraing various blocks")
    demo_possibilities(2, 0)
    demo_possibilities(2, 4)

    # draw_boxes("Demonstraing Custom Exceptions")
    # demo_custom_exceptions(-1)
    # demo_custom_exceptions(2.3)
