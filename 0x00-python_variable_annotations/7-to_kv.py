#!/usr/bin/env python3
"""python annotaion with or"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """learn how to return type or type"""
    return (k, v ** 2)