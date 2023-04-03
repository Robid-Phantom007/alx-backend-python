#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
Returns an integer
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    waits for a random delay between 0 and max_delay seconds and
    eventually returns it.
    """
    rand_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
