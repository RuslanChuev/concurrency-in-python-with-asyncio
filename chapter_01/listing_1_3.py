import threading


def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}!')


hello_thread1 = threading.Thread(target=hello_from_thread)
hello_thread1.start()

hello_thread2 = threading.Thread(target=hello_from_thread)
hello_thread2.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread is {thread_name}')

hello_thread1.join()
hello_thread2.join()
