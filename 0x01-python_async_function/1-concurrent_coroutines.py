#!/usr/bin/env python3
'''
execute multiple coroutines at the same time with async
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n():
    '''
    should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    '''

