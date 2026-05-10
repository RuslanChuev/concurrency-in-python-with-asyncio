import sys
import os
import asyncio

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь можно использовать абсолютный импорт вместо относительного
from util.delay_functions import delay


async def hello_every_second():
    for i in range(4):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())
