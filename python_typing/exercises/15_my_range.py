# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
from typing import Generator

def my_range(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end):
        yield i


my_range(1, 4)
