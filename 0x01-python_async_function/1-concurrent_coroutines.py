#!/usr/bin/env python3
"""execute multible corotuines"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute mulitible"""
    arr = []
    for i in range(n):
        arr.append(await(wait_random(max_delay)))
    return arr
