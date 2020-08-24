import numpy as np  # type: ignore
from typing import Union, List, Callable


# takes in an integer & returns an integer
def factorial(val: int) -> int:
    if val<0:
        raise ValueError("factorial() not defined for negative numbers")
    if val==0:
        return 1
    return val*factorial(val-1)


# function takes in either integer or float & returns a float
def square_root(val: Union[int, float]) -> float:
    return np.sqrt(val)


# function takes in a function, list of integer or floats & returns a list of float
def map_square_root(fn: Callable, values: List[Union[int, float]]) -> List[float]:
    return [fn(x) for x in values]


if __name__ == "__main__":
    print(f"Factorial: {factorial(3)}")
    print(f"Square Root: {square_root(4)}")
    print(f"Mapped Square Roots: {map_square_root(square_root, [0, 1, 2, 3.5, 5.6])}")
