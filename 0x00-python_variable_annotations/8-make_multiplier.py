#!/usr/bin/env python3
"""return function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function"""
    return lambda x: x * multiplier
