#!/usr/bin/env python3
"""complex annotaion"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of floatss"""
    sum: float = 0.0
    for x in input_list:
        sum += x
    return sum
