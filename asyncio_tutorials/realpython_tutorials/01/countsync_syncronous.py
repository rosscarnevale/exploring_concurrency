'''
This examples are useful to show the role played by asyncio 
it's not concurrency but it uses waiting time for a function to execute another one
to reduce this way the lagging

This example prints two strings "One" and "Two" 3 times the following way:
One
Two
One
Two
One
Two
countsync_syncronous.py executed in 3.02 seconds.
comparing with asyncronous version the sync version runs the other instances of the function during the sleep


'''
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")