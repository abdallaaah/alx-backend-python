#!/usr/bin/env python3
"""this is first task of async await"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """this the basics of the async wait"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
