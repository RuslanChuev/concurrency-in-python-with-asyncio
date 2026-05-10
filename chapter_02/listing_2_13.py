import sys
import os
import asyncio

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь можно использовать абсолютный импорт вместо относительного
from util import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.TimeoutError:
        print("Task took longer than five seconds!")
        result = await task
        print(result)


asyncio.run(main())
