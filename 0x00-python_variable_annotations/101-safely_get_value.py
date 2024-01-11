#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
     return values, add type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
