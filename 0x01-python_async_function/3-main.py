#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-task').task_wait_random


async def task(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)