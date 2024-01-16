#!/usr/bin/env python3
'''
imports async_comprehension to run with coroutine measure_runtime.
async_comprehension is executed four times in parallel using asyncio.gather
measures the total runtime and returns it
'''

import asyncio
from time import time
from importlib import import_module as using

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''returns time taken to execute comprehension
    '''
    start_time = time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            )
    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime
