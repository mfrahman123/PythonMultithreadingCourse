import asyncio
import time

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)


async def print_numbers(num):
    for i in range(num):
        print(i)

async def main():

    start_time = time.time()

    task1 = asyncio.create_task(greetings("Hello"))
    task2 = asyncio.create_task(greetings("World"))

    await task1
    await task2

    end_time= time.time()

    print("Control returned to main\n")
    print("total: ", end_time-start_time)

asyncio.run(main())