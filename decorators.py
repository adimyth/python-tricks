"""
https://realpython.com/primer-on-python-decorators/

Functions
---------
In Python, functions are first-class objects.
This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).

**************
* Decorators *
**************
A decorator is a function that takes a function and returns another function.
Usually the decorator extends the behavior of the input function without explicitly modifying it.

Inner Function
--------------
It’s possible to define functions inside other functions. Such functions are called inner functions.
They are locally scoped and exist inside parent function as local variables. Inner functions can be called from within parent function

Returning Function
------------------
Python also allows you to use functions as return values.


*******************
* Important Steps *
*******************
1. While creating a decorator, let the inner() function accept *args and **kwargs, so that the function
which the decorator decorates around, can still accept arguments
2. Make sure the inner function returns the return value of the decorated function.
3. Decorators should use the @functools.wraps decorator, which will preserve information about the original function

Other Tips
----------
1. Decorator functions can take additional arguments. But it requires creating an additional inner function.
   * Outermost function handles arguments for wrapper
   * Inner function handles the function argument sent to wrapper
   * Innermost function accepts arguments for the passed functions
"""
import functools
import time

import inflect  # type: ignore
import numpy as np  # type: ignore

from utils import draw_boxes


def timer(func):
    # Step 4: Inner function must be decorated by functools.wraps
    @functools.wraps(func)
    # Step 1: Inner function must accept *args, **kwargs
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        values = func(*args, **kwargs)
        print(
            f"[INFO] {func.__name__!r} took {(time.perf_counter() - start_time):.6f} sc"
        )
        # Step 2: Inner function must return passed functions output
        return values

    # Step 3: Wrapper function must return inner function reference
    return inner


def repeat(num_times=4):
    def decorator_inner(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # library to convert {1:1st, 2:2nd, 3:3rd}
            p = inflect.engine()
            for i in range(1, num_times + 1):
                print(f"Calling {func.__name__!r} {p.ordinal(i)} time")
                value = func(*args, **kwargs)
            return value

        return inner

    return decorator_inner


@timer
def factorial(val: int) -> int:
    ans = 1
    for i in range(1, val):
        ans = ans * i
    return ans


@repeat(num_times=3)
def square_root(val: int) -> float:
    return np.sqrt(val)


@timer
@repeat(num_times=3)
def check_prime(val: int) -> bool:
    return not any(val // i == val / i for i in range(2, val))


if __name__ == "__main__":
    draw_boxes("Simple Decorator")
    _ = factorial(300)

    draw_boxes("Decorator with Argument")
    _ = square_root(9)

    draw_boxes("Function with multiple decorators")
    _ = check_prime(13)
