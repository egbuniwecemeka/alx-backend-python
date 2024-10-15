#!/usr/bin/env python3
""" A python module on the basics of async """

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns the delay

    Args:
    max_delay (int): Max number of seconds to wait. Default is 10

    Returns:
    float: Random value in seconds
    """
    randVal = random.uniform(0, max_delay)
    await asyncio.sleep(randVal)
    return randVal