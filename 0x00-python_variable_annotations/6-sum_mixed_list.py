#!/usr/bin/env python3
"""annotaion mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum mixed list of int and floats"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
