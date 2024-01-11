#!/usr/bin/env pythoni3
"""
function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float as input and returns a tuple.
    Args:
        k (str): The input string
        v (Union[int, float]): The input integer or float.
    """
    return k, v ** 2.0
