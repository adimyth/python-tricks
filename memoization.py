"""
Memoization is a specific form of caching that involves caching the return value
of a function based on its parameters. Caching is a more general term; for example HTTP caching
is caching, not memoization.

"Memoization" is "caching the result of a deterministic function"
that can be reproduced at any time given the same function and inputs.

Useful only if a function -
1. Is Deterministic
2. Expensive to compute
3. Called many times
"""
import functools
from typing import List

import numpy as np  # type: ignore

# deterministic function
functools.lru_cache(maxsize=None)


def factorial(val: int) -> int:
    if val < 0:
        raise ValueError("factorial() not defined for negative numbers")
    if val == 0:
        return 1
    return val * factorial(val - 1)


# non-deterministic function
def random_selection(min_val: int, max_val: int) -> List[float]:
    values = np.random.randint(low=min_val, high=max_val, size=100)
    return [factorial(x) for x in values]
