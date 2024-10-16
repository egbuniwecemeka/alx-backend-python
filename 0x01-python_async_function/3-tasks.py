#!/usr/bin/env python3
""" A python script that takes an integer and rreturns an asyncio.Task """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ 
    takes an integer and returns a asyncio.Task

    Args:
    max_delay (int): Max delay for task

    Returns:
    Returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
