import threading
import time

sem = threading.Semaphore()


def fun1(run_event):
    while run_event.is_set():
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2(run_event):
    while run_event.is_set():
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


def main():
    run_event = threading.Event()
    run_event.set()
    t1 = threading.Thread(target=fun1, args=(run_event,))
    t1.start()
    t2 = threading.Thread(target=fun2, args=(run_event,))
    t2.start()

    try:
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        print("attempting to close threads...")
        run_event.clear()
        t1.join()
        t2.join()
        print("threads successfully closed")


if __name__ == '__main__':
    main()
