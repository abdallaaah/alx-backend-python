#!/usr/bin/env python3
"""execute multible corotuines"""
from typing import List
import time
import random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute mulitible"""
    arr = []
    for i in range(n):
        x = random.uniform(0, max_delay)
        await time.sleep(x)
    return arr
