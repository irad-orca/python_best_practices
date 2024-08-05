# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
from typing import Dict

def get_dict_str_str(d: Dict[str, str]) -> None:
    pass  # The implementation doesn't matter here


get_dict_str_str({"a": "b"})
get_dict_str_str({})


def get_dict_str_int(d: Dict[str, int]) -> None:
    pass  # The implementation doesn't matter here


get_dict_str_int({"a": 1})
get_dict_str_int({})
