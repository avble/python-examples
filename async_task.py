import threading
import asyncio
import time

async def say_after(id, delay):
    print(f"{time.strftime('%X')} Task {id} thread-id: {threading.get_ident()} enter >>")
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')} Task {id} thread-id: {threading.get_ident()} leave <<")

async def main():
    task1 = asyncio.create_task(
        say_after("t-1", 3,))

    task2 = asyncio.create_task(
        say_after("t-2", 3,))

    print(f"{time.strftime('%X')} Task 0   thread-id: {threading.get_ident()} end")
    # Wait until both tasks are completed
    await task1
    await task2

    print(f"{time.strftime('%X')} Task 0   thread-id: {threading.get_ident()} end")

asyncio.run(main())
