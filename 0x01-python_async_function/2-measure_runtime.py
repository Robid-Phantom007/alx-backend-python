#!/usr/bin/env python3
"""
Module 2-measure_runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    start = time.perf_counter()
    wai_t = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return ((end - start) / n)
