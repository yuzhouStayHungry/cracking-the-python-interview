from _thread import start_new_thread, allocate_lock
import time

num = 0


# mutex = allocate_lock()


def plus_one():
    global num
    # mutex.acquire()

    for i in range(1000000):
        num += 1
    # mutex.release()


def minus_one():
    global num
    # mutex.acquire()
    for i in range(1000000):
        num -= 1
    # mutex.release()


def main():
    start_new_thread(plus_one, ())
    start_new_thread(minus_one, ())
    time.sleep(3)
    print(num)


if __name__ == '__main__':
    main()
