import math
from threading import Thread
from queue import Queue

def multithreading_factorial():
    while True:
        item = queue_for_threads.get()
        factorial_result = math.factorial(item)
        print("Факториал числа {} равен {}:  ".format(item, factorial_result))
        queue_for_threads.task_done()

COUNT_WORKERS = 5

queue_for_threads = Queue()

for i in range(COUNT_WORKERS):
    new_thread = Thread(target=multithreading_factorial)
    new_thread.daemon = True
    new_thread.start()

for item in range(10, 100, 5):
    queue_for_threads.put(item)

queue_for_threads.join()
