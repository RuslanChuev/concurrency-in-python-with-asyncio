import sys
import os
import asyncio

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь можно использовать абсолютный импорт вместо относительного
from util.delay_functions import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout!')
        print(f'Was the task cancelled? {delay_task.cancelled()}')


asyncio.run(main())
