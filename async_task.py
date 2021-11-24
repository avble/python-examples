import asyncio
import time

async def say_after(id, delay):
    print(f"{time.strftime('%X')} Task {id} enter >>")
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')} Task {id} leave <<")

async def main():
    task1 = asyncio.create_task(
        say_after("t-1", 3,))

    task2 = asyncio.create_task(
        say_after("t-2", 3,))

    print(f"main start - {time.strftime('%X')}")
    # Wait until both tasks are completed
    await task1
    await task2

    print(f"main end - {time.strftime('%X')}")

asyncio.run(main())

# Sample output
# main start - 13:21:34
# 13:21:34 Task t-1 enter >>
# 13:21:34 Task t-2 enter >>
# 13:21:37 Task t-1 leave <<
# 13:21:37 Task t-2 leave <<
# main end - 13:21:37