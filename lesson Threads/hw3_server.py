"""
В процессе работы было замечено, что вплоть до элемента с индексом 10000
вычисление факториала одним процессом выполняется быстрее. От 20000 и более
два процесса уже помогают распараллелить выполнение задачи и время выполнения
значительно уменьшается.

10000-ый элемент:
два процесса - 0.059735774993896484
один процесс - 0.04614973068237305

20000-ый элемент:
два процесса - 0.1310279369354248
один процесс - 0.19257664680480957

50000-ый элемент:
два процесса - 0.8486580848693848
один процесс - 1.311173915863037

100000-ый элемент:
два процесса - 3.587493658065796
один процесс - 5.937816143035889

500000-ый элемент:
два процесса - 120.58638739585876
один процесс - 199.34530305862427
"""

from socket import *
from multiprocessing import Queue, Process
import hashlib
import time


def odd_factorial(q, number):
    """for multiprocessing"""
    number = int(number)
    total = 1
    for i in range(1, number + 1):
        if i % 2 == 1:
            total *= i
    q.put(total)


def even_factorial(q, number):
    """for multiprocessing"""
    number = int(number)
    total = 1
    for i in range(1, number + 1):
        if i % 2 == 0:
            total *= i
    q.put(total)


def factorial(number):
    """to compare with multiprocessing"""
    number = int(number)
    total = 1
    while number != 1:
        total = total * number
        number = number - 1
    return total


def hashMD5(number):
    """calculate md5 hash"""
    number = int(number)
    m = hashlib.md5()
    m.update(str(number).encode('utf-8'))
    return m.hexdigest()


def main_server_function(port: int = 8000, num_of_workers: int = 2):
    host = '127.0.0.1'
    s = socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("connection from: ", str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user: " + str(data.decode()))

        time_start = time.time()
        q = Queue()
        p1 = Process(target=odd_factorial, args=(q, data))
        p2 = Process(target=even_factorial, args=(q, data))
        p1.start()
        p2.start()
        data = q.get() * q.get()
        p1.join()
        p2.join()
        data = hashMD5(data)
        time_end = time.time()

        # time_start = time.time()
        # data = factorial(data)
        # data = hashMD5(data)
        # time_end = time.time()

        print('time of calculatings: ' + str(time_end - time_start))
        print("sending: " + str(data))
        c.send(str(data).encode())
    c.close()


main_server_function()
