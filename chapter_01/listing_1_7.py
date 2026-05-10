import time
import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


sync_start = time.time()

read_example()  # 1
read_example()  # 2
read_example()  # 3
read_example()  # 4
read_example()  # 5
read_example()  # 6
read_example()  # 7
read_example()  # 8
read_example()  # 9
read_example()  # 10

sync_end = time.time()

print(f'Running synchronously took {sync_end - sync_start:.4f} seconds.')
