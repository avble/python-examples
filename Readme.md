# Asyncio 
# Coroutine
``` python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())

```

## Notes 
``` async def tested()``` is to define a coroutine function tested
``` tested() ``` is to create a coroutine object. So it is not called at all.
``` await nested() ``` is to create a coroutine object, then call, then wait until the coroutine complete


## Task
``` python
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
```

``` bash
16:09:40 Task 0   thread-id: 140307003934528 end
16:09:40 Task t-1 thread-id: 140307003934528 enter >>
16:09:40 Task t-2 thread-id: 140307003934528 enter >>
16:09:43 Task t-1 thread-id: 140307003934528 leave <<
16:09:43 Task t-2 thread-id: 140307003934528 leave <<
16:09:43 Task 0   thread-id: 140307003934528 end
```

## Notes:
- As above observation, 