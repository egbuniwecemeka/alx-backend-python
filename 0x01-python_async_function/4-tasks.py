#!/usr/bin/env python3
""" A python script exhibiting concurrent/asynchronous operations """

import asyncio
from typing import List
from bisect import insort

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ 
    Spawns task_wait_n n times with the specified delay time
    Also, returns a list of all delay values as floats

    Args:
    n (int): Number ot times to spawn task_wait_n
    max_delay: Maximum delay time for task_wait_n

    Return:
    List of all delay values (floats)
    """
    spawn = [task_wait_n(max_delay) for _ in range(n)]

    # run spqwned tasks concurrently and collect their values
    delays = await asyncio.gather(*spawn)

    # Manual sorting without using sort()
    sorted_task = []
    for delay in delays:
        insort(sorted_task, delay)

    return sorted_task