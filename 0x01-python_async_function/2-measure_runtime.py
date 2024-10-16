#!/usr/bin/env python3
""" A python script that measures total execution runtime"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    synchronous function that measures the execution runtime for
    wait_n(n, max_delay)

    Args:
    n (int): Number of tasks to run
    max_delay (int): Max delay for wait_random

    Returns:
    float: Average time per task
    """
    # Record the start time
    start_time = time.time()

    # synchronously run wait_n
    asyncio.run(wait_n(n, max_delay))

    # Record end time
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
