#!/user/bin/env python3
"""crate async function with ayncio.create_task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay):
    """regular wait"""
    return asyncio.create_task(wait_random(max_delay))