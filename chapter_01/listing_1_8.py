import time
import threading
import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)
thread_3 = threading.Thread(target=read_example)
thread_4 = threading.Thread(target=read_example)
thread_5 = threading.Thread(target=read_example)
thread_6 = threading.Thread(target=read_example)
thread_7 = threading.Thread(target=read_example)
thread_8 = threading.Thread(target=read_example)
thread_9 = threading.Thread(target=read_example)
thread_10 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_9.start()
thread_10.start()

print('All threads running!')

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()
thread_9.join()
thread_10.join()

thread_end = time.time()

print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')
