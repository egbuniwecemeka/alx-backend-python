#!/usr/bin/env python3
""" A python script executing concurrent coroutines"""

import asyncio
from typing import List
from bisect import insort

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times, with the specified max_delay
    It also returns the list of delay floats in ascending order

    Args:
    n (int): Number of times to spawn wait_random
    max_delay (int):max delay for wait_random

    Return:
    List of delays
    """
    spawned = [wait_random(max_delay) for _ in range(n)]

    # run spawned tasks concurrently, and collect their values
    delays = await asyncio.gather(*spawned)

    # Manual sorting without using sort()
    sorted_delay = []
    for delay in delays:
        insort(sorted_delay, delay)

    return sorted_delay
