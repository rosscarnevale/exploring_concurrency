'''
This examples are useful to show the role played by asyncio 
it's not concurrency but it uses waiting time for a function to execute another one
to reduce this way the lagging

This example prints two strings "One" and "Two" 3 times the following way:
One
One
One
Two
Two
Two
countsync_asyncronous.py executed in 1.02 seconds.


'''

import time
import asyncio
import datetime

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
