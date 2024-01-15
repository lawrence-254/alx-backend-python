#!/usr/bin/env python3
'''
asyncnorous coroutine that returns a value of seconds waited
'''
import asyncio
import random


async def wait_random(max_delay : float = 10) -> float :
    '''
    a function that waits for a defined amount of seconds,
    defaulted to 10 seconds and returns the seconds waited for
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
