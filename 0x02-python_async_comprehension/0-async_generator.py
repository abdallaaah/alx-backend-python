#!/usr/bin/env python3
"""the yeild understanding"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times"""
    for i in range(2):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
