#!/usr/bin/env python3
'''
a coroutine that loops 10 times, asynchronously waits waits one second
then yields a random number between 0 and 10
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    yields a random number between 0 and 10 ten times
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
