"""
Generator function can suspend and resume. They can yield & pick up from where it left.
It allows us to generate list of elements on the fly.
"""
from typing import Generator, List

from rich import print

from utils import draw_boxes


def gen(n: int) -> Generator:
    for i in range(n):
        print(f"Generator {i}")
        yield i


def fun(n: int) -> List[int]:
    numbers = []
    for i in range(n):
        print(f"Function {i}")
        numbers.append(i)
    return numbers


def non_finite_gen() -> Generator:
    i = 0
    while True:
        print(f"Infinite Gen: {i}")
        i = i + 1
        yield i


if __name__ == "__main__":
    draw_boxes("Generator & Function Paired")
    for _, _ in zip(gen(5), fun(5)):
        pass

    draw_boxes("Generator Paired")
    for _, _ in zip(gen(5), gen(10)):
        # looping through a generator implicitly calls next()
        pass

    draw_boxes("Using StopIteration on a finite generator")
    fin_gen = gen(5)
    for i in range(10):
        try:
            next(fin_gen)
        except StopIteration:
            print("Breaking loop as generator is exhausted")
            break

    draw_boxes("Gracefully exiting an infinite generator using close()")
    fin_gen = non_finite_gen()
    for i in range(10):
        next(fin_gen)
        if i > 5:
            fin_gen.close()
