import asyncio

async def main():
    my_future = asyncio.Future()   # now there is a running loop

    print(f'Is my_future done? {my_future.done()}')
    my_future.set_result(42)
    print(f'Is my_future done? {my_future.done()}')
    print(f'What is the result of my_future? {my_future.result()}')

asyncio.run(main())
