#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
Returns a list of all delays
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    return the list of all the delays (float values)
    ist of the delays should be in ascending order without
    using sort() because of concurrency
    """
    result = []
    aws = [wait_random(max_delay) for i in range(n)]
    for t in asyncio.as_completed(aws):
        result.append(await t)
    return result
