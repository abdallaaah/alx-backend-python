#!/usr/bin/env python3
"""complex annotaion"""


def sum_list(list: [float]) -> float:
    """return sum of floats"""
    sum: float = 0.0
    for x in list:
        sum += x
    return sum
