#!/usr/bin/env python3
'''
Measure the runtime
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    '''
    start_exe_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_exe_time = time.time()

    time_to_run = end_exe_time - start_exe_time
    average_exec_time = time_to_run / n
    return average_exec_time
