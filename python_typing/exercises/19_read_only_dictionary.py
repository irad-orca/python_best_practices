# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html

# This is new:
# https://mypy.readthedocs.io/en/stable/more_types.html
from typing import Mapping

def read_only_dictionary(d: Mapping[str, int]) -> None:
    pass  # The implementation doesn't matter here


read_only_dictionary(d={"a": 1})
