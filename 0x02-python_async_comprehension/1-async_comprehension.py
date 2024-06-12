#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a coroutine"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers"""
    return [_ async for _ in async_generator()]
