# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
from typing import TypeVar

T = TypeVar("T", int, str)

def add_int_str(a: T, b: T) -> T:
    return a + b


assert add_int_str(1, 1) == 2
assert add_int_str("Swimm ", "is awesome") == "Swimm is awesome"
