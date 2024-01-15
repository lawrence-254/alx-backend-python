#!/usr/bin/env python3
'''
imports from wait_n
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    return the list of all the delays (float values).
    The list of the delays should be in ascending order without
    using sort() because of concurrency.
    '''
    delays = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
            )
    return sorted(delays)
