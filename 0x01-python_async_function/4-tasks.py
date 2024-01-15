#!/usr/bin/env python3
'''
imports from wait_n
'''
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
